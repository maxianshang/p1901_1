import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('10.1.0.103',8080))
s.listen(1)

while 1:
    client_contion,client_addr = s.accept()
    request = client_contion.recv(1024)
    print(request)
    http = b"""
    HTTP/1.1 200 OK\r\n
	\r\n
	Hello,world!
    """
    client_contion.send(http)
    client_contion.close()