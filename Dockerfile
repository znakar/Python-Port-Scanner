FROM python:3.13-slim-trixie

WORKDIR /pps

RUN apt-get update && apt-get install -y git --no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

RUN python3 --version && git --version

RUN git clone https://github.com/znakar/Python-Port-Scanner

WORKDIR Python-Port-Scanner

RUN pip install git+https://github.com/tqdm/tqdm.git --break-system-packages 

ENTRYPOINT ["python3", "port-scanner.py"]

CMD ["-p", "tcp", "-t google.com", "-r", "1-1000", "-w", "300"]
