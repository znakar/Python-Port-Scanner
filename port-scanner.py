import socket
import sys
import datetime
from concurrent.futures import ThreadPoolExecutor


MAX_WORKERS = 100
MESSAGE = b'Ping...'
date_time = datetime.datetime.now()

print(date_time)

host = input("Enter IP address: ")
port_range = '0-1025'

port_range = port_range.split('-')
start_port = int(port_range[0])
end_port = int(port_range[1])

def scanhost_tcp(host, port):
     
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        result = s.connect_ex((host, port))
    if result == 0:
        return(f"Port {port}/TCP open")
    else:
        None
    

def scanhost_udp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        s.settimeout(0.4)
        try:
            s.sendto(MESSAGE, (host, port))
            host, port = s.recvfrom(1024)
            return (f"Port {port}/UDP open")
        except socket.timeout:
            return (f"Port {port}/UDP open or filtered (no response)")
        except ConnectionRefusedError:
            return (f"Port {port}/UDP closed")


list_of_ports = [(host, port) for port in range(start_port, end_port + 1)]

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:    
    tcp_result = list(executor.map(lambda args: scanhost_tcp(*args), list_of_ports))
    
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    udp_result = list(executor.map(lambda args: scanhost_udp(*args), list_of_ports))
    
    all_scan_results = tcp_result + udp_result
    all_scan_results_sorted = sorted(
        [result for result in all_scan_results if result],
        key=lambda x: (
          int(x.split()[1].split('/')[0]), 
          0 if "/TCP" in x else 1
    )
)   
    for line in all_scan_results_sorted:
        print(line)






