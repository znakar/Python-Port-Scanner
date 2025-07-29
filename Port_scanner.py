import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

host = "127.0.0.1"
port = 9090
timeout = 10

try:
    with socket.create_connection((host, port), timeout=timeout):
        print(f"Порт {port} открыт")
except (socket.timeout, ConnectionError, OSError):
    print(f"Порт {port} закрыт")


















# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

