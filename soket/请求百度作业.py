import  socket

# 报文和传送内容 中间空行
baowen = """
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 03 Apr 2019 08:11:46 GMT
Content-Type: text/html; charset=UTF-8

hello wold

"""
# 创建套接字  默认ipv4 tcp协议

ss = socket.socket()

addr = ('0.0.0.0',9090)
# 绑定端口
ss.bind(addr)
ss.listen(5)

while 1:
    # 接受监听的信息
    conn,addr =ss.accept()

    recv_data = conn.recv(1024)
    print(recv_data.decode())
    # 回送报文和内容
    conn.send(baowen.encode())


