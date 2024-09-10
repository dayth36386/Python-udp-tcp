import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 5555
s.bind((host,port))
print("Sever Started")

while True:
    print("Waiting...")
    data, address = s.recvfrom(1042)
    # print('From client: {}'.format(address))
    print('Data: {}'.format(data.decode()))

    msg = 'Server: Welcome to Server'
    s.sendto(msg.encode(), address)