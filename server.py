import socket
#TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5555
s.bind((host,port))
s.listen(1)
print("Sever Starting...")
while True:
    print("Waiting...")
    con, address = s.accept()
    print("Connected from{}".format(address))
    server_msg = 'Welcome to My Server S2'
    con.send(server_msg.encode())
    data = con.recv(1042).decode()
    print(data)

