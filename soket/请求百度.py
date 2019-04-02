# 写一个socket用来请求百度网页,并把请求下来的报文体部分保存

import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('123.206.1.112',80))
    headers = b"GET /114633/ HTTP/1.1\r\nHost: blog.jobbole.com\r\nConnection: closed\r\n" \
            b"Cache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: " \
            b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) " \
            b"Chrome/73.0.3683.86 Safari/537.36\r\nAccept: text/html,application/xhtml+xml," \
            b"application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n\r\n"
    s.send(headers)
    res = b''
    while 1:
        msg = s.recv(1024)
        if not msg:
            break
        res+=msg
    s.close()
    print(res.decode())
if __name__ == '__main__':
    main()