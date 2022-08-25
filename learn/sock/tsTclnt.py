# -*- coding: utf-8 -*-
from socket import *

"""
创建tcp客户端伪代码：
cs = socket() # 创建客户端套接字
cs.connect() # 尝试连接服务器
comm_loop: # 通信循环
cs.send()/cs.recv() # 对话（发送/接收）
cs.close() # 关闭客户端套接字
"""


HOST = 'localhost'
PORT = 12451
# 缓冲区大小设置为 1KB, 可以根据网络性能和程序需要改变这个容量
BUFSIZE = 1024
ADDR = (HOST, PORT)


def run():
    tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
    # 主动发起 TCP 服务器连接
    tcp_cli_sock.connect(ADDR)

    while True:
        data = input('> ')
        if not data:
            break
        data = bytes(data, 'utf-8')
        # 发送 TCP 消息
        tcp_cli_sock.send(data)
        # 接收 TCP 消息
        data = tcp_cli_sock.recv(BUFSIZE)
        if not data:
            break
        print(data.decode('utf-8'))

    tcp_cli_sock.close()


if __name__ == '__main__':
    run()

