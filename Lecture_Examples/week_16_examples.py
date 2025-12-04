import socket
from urllib.request import urlopen
import re as r

def get_external_ip() -> str:
    return (r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)')
            .search(str(urlopen('http://checkip.dyndns.com').read())).group(1))
def get_internal_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
def main():
    print(f'External IP: {get_external_ip()}')
    print(f'Internal IP: {get_internal_ip()}')
if __name__ == "__main__":
    main()