import socket
import datetime
import concurrent.futures
import argparse
import sys
from argparse import Namespace
from concurrent.futures import ThreadPoolExecutor

try:
    from tqdm import tqdm
except ImportError:
    print("Error: Module 'tqdm' is not found.")
    print("Please run the following command in the terminal: pip install tqdm")
    sys.exit(1)



MESSAGE = b'Ping...'

parser = argparse.ArgumentParser(description='Simple port scanner')


parser.add_argument('-p', '--protocol', required=True, choices=['tcp', 'udp'], help='Select protocol - tcp/udp')
parser.add_argument('-t', '--target', required=True, type=str, help='Specify IP address')
parser.add_argument('-r', '--range', type=str, default='1-1024', help='Sepcify the port range to scan (default: 1-1024)')
parser.add_argument('-w', '--workers',type=int, default=200, help='number of worker threads performing parallel execution of tasks (default: 200)')

args: Namespace = parser.parse_args() 

host = args.target
port_range = args.range

port_range = port_range.split('-')
start_port = int(port_range[0])
end_port = int(port_range[1])

list_of_ports = [(host, port) for port in range(start_port, end_port + 1)]

workers = min(args.workers, len(list_of_ports))



def scanhost_tcp(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            result = s.connect_ex((host, port))
        if      result == 0:
            return(f"Port {port}/TCP open")
        else:
            return(f"Port {port}/TCP closed")
    except ConnectionRefusedError:
        return(f"Port {port}/TCP closed (Reset by Firewall)")
    except socket.gaierror:
        return("Error when receiving IP address")
    except socket.timeout:
        return(f"Port {port}/TCP (Host not responding)")
    except ConnectionResetError:
        return(f"Port {port}/TCP (Reset)")
    except Exception as e:
        return(f"Port {port}/TCP filtered/error ({e.__class__.__name__})")
    

def wrapper_scan_tcp(args):
    host, port = args
    return scanhost_tcp(host, port)


def scanhost_udp(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
            s.settimeout(3)
            s.sendto(MESSAGE, (host, port))
            host, addr = s.recvfrom(1024)
            return (f"Port {port}/UDP open (response from {addr[0]}:{addr[1]})")               
    except socket.timeout:
        return (f"Port {port}/UDP open or filtered (no response)")
    except ConnectionRefusedError:
        return (f"Port {port}/UDP closed")
    except ConnectionResetError:
        return (f"Port {port}/UDP closed (Reset)")
    except Exception as e:
        return (f"Port {port}/UDP filtred/error ({e.__class__.__name__})")       

def wrapper_scan_udp(args):
    host, port = args
    return scanhost_udp(host, port)


if args.protocol == 'tcp':
    future_results = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for task_args in tqdm(list_of_ports, desc="Start TCP", unit='ports', ncols=120):
            fut = executor.submit(wrapper_scan_tcp, task_args)  
            future_results[fut] = task_args

    print("--- TCP Results ---")
    for future in concurrent.futures.as_completed(future_results):
        host_arg, port_number = future_results[future]
        try:
            output = future.result()
        except Exception as exc:
            print(f"Port {port_number}/TCP generated an unhandled exception: {exc.__class__.__name__}")
        else:
            print(output)

elif args.protocol == 'udp':
    future_results = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for task_args in tqdm(list_of_ports, desc="Start UDP", unit='ports', ncols=120):
            fut = executor.submit(wrapper_scan_udp, task_args)
            future_results[fut] = task_args

    print("--- UDP Results ---")
    for future in concurrent.futures.as_completed(future_results):
        host_arg, port_number = future_results[future]
        try:
            output = future.result()
        except Exception as exc:
            print(f"Port {port_number}/UDP generated an unhandled exception: {exc.__class__.__name__}")
        else:
            print(output)

print(datetime.datetime.now())