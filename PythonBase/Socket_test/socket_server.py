__author__ = "lfs"

import socket

server = socket.socket()
server.bind(('localhost', 6969))
server.listen(5)

print("我要开始等电话了")
while True:
    conn, addr = server.accept()
    print("电话进来了")
    while True:
        data = conn.recv(1024)
        print("recv:", data)
        if not data:
            print("client has lost...")
            break
        conn.send(data.upper())

server.close()