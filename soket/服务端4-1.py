import socket
def main():
    # 创建服务端套接字
    f_seler = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    f_add = ('',6969)
    f_seler.bind(f_add)  # 将本地地址与一个socket绑定在一起
    print('服务已开启')
    f_seler.listen()  # 监听
    conn,conn_addr = f_seler.accept()
    while 1:
        try:
            # 收到的消息
            msg = conn.recv(65535)
            msg.decode()
            print('收到{}的消息:{}'.format(conn_addr,msg))
            # 返回的消息
            return_msg = '消息收到了'+msg
            conn.send(return_msg.encode())
        except Exception:
            break
    print('----1-----')

    conn.close()
    f_seler.close()
    print(conn_addr)


if __name__ == '__main__':
    main()
