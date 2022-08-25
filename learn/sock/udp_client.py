# -*- coding: utf-8 -*-
from socket import *
from udp_server import UDP_ADDRESS, UDP_BUFSIZE

"""
创建udp client伪代码：
cs = socket() # 创建客户端套接字
comm_loop: # 通信循环
cs.sendto()/cs.recvfrom() # 对话（发送/接收）
cs.close() # 关闭客户端套接字
"""


def run():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input('> ')
        if not data:
            break
        data = bytes(data, 'utf-8')
        udp_socket.sendto(data, UDP_ADDRESS)
        rec_data, addr = udp_socket.recvfrom(UDP_BUFSIZE)
        if not rec_data:
            break
        print("server result:", rec_data)
    udp_socket.close()


if __name__ == '__main__':
    run()

