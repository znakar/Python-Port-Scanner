# Python Port Scanner
[![Python](https://img.shields.io/badge/python-3.13.1-3670A0?style=for_the-badge&logo=python&logoColor=ffdd54)](https://www.python.org) \
[![Licence](https://img.shields.io/github/license/znakar/Port_scanner?style=for-the-badge)](./LICENSE) \
[![Github Stars](https://img.shields.io/github/stars/znakar/Port_scanner)](https://github.com/znakar/Port_scanner/stargazers)
## A lightweight Python port scanner with TCP and UDP support. Suitable for basic network auditing and learning.

The project demonstrates:

* Creating network connections
* Checking port availability
* TCP and UDP scanning
* Multithreading

## Demonstration of work

**Scan by ip address**
![Демонстрация сканирования по IP](https://github.com/user-attachments/assets/a1da5160-05e5-4e94-98bc-5f8622a05a59)

**Scan by domain name**
![Демонстрация сканирования по доменному имени](https://github.com/user-attachments/assets/8649a4b5-6b90-4b6d-928f-3cac30b7cf86)


## Installation and launch
### requirements
- [Python 3.13.1](https://www.python.org/downloads/)

### Windows 10/11 <img width="20" height="20" alt="icons8-windows-10-48 (1)" src="https://github.com/user-attachments/assets/cfbbaca1-024c-4d53-b57d-f32455689e4e" /> 

1. Download ZIP, Code → [Download Zip](https://github.com/znakar/Port_Scanner)
2. Unzip the archive to a convenient location
3. Open a command prompt (Win + r → cmd)
4. Go to the project folder (cd "path\to\project")
5. Run python port_scanner.py


### Ubuntu: latest version <img width="24" height="24" alt="icons8-linux-24" src="https://github.com/user-attachments/assets/28b77c38-a02b-475e-a196-fe6c57407954" />
1. apt update
2. apt install python3 python3-pip git
3. git clone https://github.com/znakar/Port_Scanner
4. cd Port_Scanner/
5. python3 port-scanner.py

## Find a bug? <img width="24" height="24" alt="icons8-bug-24 (1)" src="https://github.com/user-attachments/assets/2b26c80d-bcb4-43cf-9df3-01510d9335a4" />




If you found ad issue or would like to submit an improvment to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created.

## Known issues (Work in Progress) <img width="24" height="24" alt="icons8-in-progress-24" src="https://github.com/user-attachments/assets/2cd3ae99-dbe3-484b-b4c9-0b7dafe9f7e8" />

  <img width="12" height="12" alt="icons8-error-12" src="https://github.com/user-attachments/assets/f8848112-6724-4c10-97b0-69104777eafc" /> Ports are not listed in order \
  <img width="12" height="12" alt="icons8-error-12" src="https://github.com/user-attachments/assets/897aed0a-099c-4155-bd46-732d90a7c621" /> UDP scan does not guarantee that the port is open \
  <img width="12" height="12" alt="icons8-error-12" src="https://github.com/user-attachments/assets/d19599ce-1592-479e-aa2a-b5c4f0603577" /> After execution on Linux, an error is thrown: OSError: [Errno 22]
