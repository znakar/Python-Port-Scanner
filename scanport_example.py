import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

MAX_WORKERS = 100




def generate_port_chunks(port_range):
    port_ranges = port_range.split('-')
    port_chunks = []

    chunk_size = int((int(port_ranges[1]) - int(port_ranges[0])) / MAX_WORKERS) 

    for i in range (MAX_WORKERS):
        start = int(port_ranges[0]) + (chunk_size * i)
        end = start + chunk_size
        port_chunks.append([start, end])
    return port_chunks

def scan(ip_address, port_chunk):
    print(f"[~] Scanning {ip_address} from {port_chunk[0]} to {port_chunk[1]}.")
    for port in range(int(port_chunk[0]), int(port_chunk[1])):
        try:
            scan_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan_socket.settimeout(2)
            scan_socket.connect((ip_address, port))
            print(f"[!] Port {port} is open")
        except:
            None

def main():
    ip_address = '192.168.0.50'
    port_range = '0-10000'

    port_chunks = generate_port_chunks(port_range)

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(scan, [ip_address] * len(port_chunks), port_chunks)

    end_time = time.time()
    print(f"Scanner {port_range[1]} ports in {end_time - start_time} seconds.")

if __name__ == '__main__':
    main()