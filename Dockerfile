FROM python:3.13-slim-trixie

WORKDIR /pps

RUN python3 --version 

COPY requirements.txt  .

RUN pip install --no-cache-dir -r requirements.txt 

RUN useradd -m scanner && chown -R scanner /pps
USER scanner

ENTRYPOINT ["python3", "port-scanner.py"]

CMD ["-p", "tcp", "-t", "google.com", "-r", "1-1000", "-w", "300"]



