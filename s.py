import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 5555
s.bind((host,port))
print("Sever Started")

while True:
    print("Waiting...")
    num1, address = s.recvfrom(1042)
    print('Receiving data ... {}'.format(num1.decode()))
    op, address = s.recvfrom(1042)
    print('Receiving data ... {}'.format(op.decode()))
    num2, address = s.recvfrom(1042)
    print('Receiving data ... {}'.format(num2.decode()))

    msg = 'Result is {}'.format(eval(str(num1.decode()) + op.decode() + str(num2.decode())))
    s.sendto(msg.encode(), address)
