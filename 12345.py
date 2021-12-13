import socket

dst = ('25.43.146.137',2020)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('25.54.47.211', 2022))
sock.sendto(bytes.fromhex('aaaa'),dst)
while True:
    data, addr = sock.recvfrom(1024)
    print(data)
    print(addr)