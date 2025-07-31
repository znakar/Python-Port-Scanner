import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor


MAX_WORKERS = 200

host = input("Введите IP-адрес: ")
port = int(input("Введите порт: "))

port_range = '0-65535'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(2)
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"Порт {port}/TCP открыт")
    else:
        print(f"Порт {port}/TCP закрыт")

