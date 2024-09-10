import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 5555
server = (host,port)
num1 = input("Enter num1: ")
s.sendto(num1.encode(), server)
op = input("Enter Operator : ")
s.sendto(op.encode(), server)
num2 = input("Enter num2: ")
s.sendto(num2.encode(), server)

data, address = s.recvfrom(1042)
print(data.decode())