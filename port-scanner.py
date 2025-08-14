import socket
import sys
import datetime
from concurrent.futures import ThreadPoolExecutor


MAX_WORKERS = 300
MESSAGE = b'Ping...'
date_time = datetime.datetime.now()

print(date_time)

host = input("Введите IP-адрес: ")
port_range = '0-1025'


port_range = port_range.split('-')
start_port = int(port_range[0])
end_port = int(port_range[1])

def scanhost_tcp(host_port):
    host, port = host_port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        result = s.connect_ex((host, port))
    if result == 0:
        print(f"Порт {port}/TCP open")
    else:
        pass
    

def scanhost_udp(host_port):
    host, port = host_port
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        s.settimeout(1)
        try:
            s.sendto(MESSAGE, (host, port))
            print(f"Порт {port}/UDP open")
        except socket.timeout:
            print(f"Порт {port}/UDP открыт или фильртуется (нет ответа)")
        except ConnectionRefusedError:
            print(f"Порт {port}/UDP closed")


list_of_ports = [(host, port) for port in range(start_port, end_port + 1)]

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:    
    list(executor.map(scanhost_tcp, list_of_ports))

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    list(executor.map(scanhost_udp, list_of_ports))


     


