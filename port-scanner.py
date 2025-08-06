import socket
import sys
import datetime
from concurrent.futures import ThreadPoolExecutor


MAX_WORKERS = 100

date_time = datetime.datetime.now()

print(date_time)

host = input("Введите IP-адрес: ")
port = int(input("Введите порт: "))


port_range = '0-1025'
port_range = port_range.split('-')
start_port = int(port_range[0])
end_port = int(port_range[1])

def scanhost(host_port):
    host, port = host_port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        result = s.connect_ex((host, port))
    if result == 0:
        print(f"Порт {port}/TCP открыт")
    else:
        print(f"Порт {port}/TCP закрыт")
    
scanhost((host, port))

list_of_ports = [(host, port) for port in range(start_port, end_port)]

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
     executor.map(scanhost, list_of_ports)

