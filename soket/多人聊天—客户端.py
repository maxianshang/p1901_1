
import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss.connect(('127.0.0.1', 9996))
def main():

    t1 = threading.Thread(target=conn_send,args=(ss,))
    t2 = threading.Thread(target=conn_recv,args=(ss,))
    t1.start()
    t2.start()
    print('客户端启动')
    t1.join()
    t2.join()
    print('客户端停止')

def conn_send(ss):
    while 1:
        msg = input('请输入要发送的数据')
        try:
            ss.send(msg.encode())
        except Exception:
            break
        print('传输完成')
def conn_recv(ss):
    while 1:
        retun_msg = ss.recv(1024)

        try:
            print(retun_msg.decode())

        except Exception:
            break
        print('     ')

if __name__ == '__main__':
    main()



