import socket
#TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5555
s.connect((host,port))

data = s.recv(1042).decode()
print(data)
name = input("Enter Name : ")
s.send(name.encode())
s.close()
