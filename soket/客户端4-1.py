import socket

def main():
    # 创建套接字
    clier = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    k_addr = ('14.215.177.39',80)
    clier.connect(k_addr)
    while 1:
        try:
            msg = input('输入报文')

            clier.send(msg.encode())
            msg = clier.recv(1460)
            print('收到服务器发来的消息',msg.decode())
            clier.close()
        except Exception:
            break
    print('链接以完成')


if __name__ == '__main__':
    main()