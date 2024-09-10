import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 5555
server = (host,port)
msg = "10"
s.sendto(msg.encode(), server)

data, address = s.recvfrom(1042)
print(data.decode())