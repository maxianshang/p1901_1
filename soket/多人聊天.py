import socket
import threading

seller_lise = []
def taerad_adde(conn,addr):
    # conn。recv是从缓存区接收数据 ， 用变量接收
    msg = conn.recv(1024)
    # 返回给用户的信息
    return_msg = '地址{}的用户说:{}'.format(addr,msg.decode())
    for conn in seller_lise:
        conn.send(return_msg.encode())

# tcp 服务端
def main(adddr):
    # 创建套接字
    ss = socket.socket()
    # 绑定ip地址    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    ss.bind(adddr)
    # 设置监听
    ss.listen(5)
    print('服务器启动')
    while 1:
        # 接收用户和地址
        conn,addr = ss.accept()
        # 地址放入空列表
        seller_lise.append(conn)
        print('新来的地址{}'.format(addr))
        # 创建多线程 并传入内容和地址
        thread = threading.Thread(target=taerad_adde,args=(conn,addr))
        thread.start()


if __name__ == '__main__':
    # 设置地址
    adddr = ('127.0.0.1',9996)
    main(adddr)




