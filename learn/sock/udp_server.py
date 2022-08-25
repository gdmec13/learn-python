# -*- coding: utf-8 -*-
from socket import *

"""
创建udp服务端伪代码：
ss = socket() # 创建服务器套接字
ss.bind() # 绑定服务器套接字
inf_loop: # 服务器无限循环
cs = ss.recvfrom()/ss.sendto() # 关闭（接收/发送）
ss.close() # 关闭服务器套接字
"""

UDP_HOST = "localhost"
UDP_PORT = 34141
UDP_BUFSIZE = 1024
UDP_ADDRESS = (UDP_HOST, UDP_PORT)


def run():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(UDP_ADDRESS)

    while True:
        print("waiting message ....")
        data, addr = udp_socket.recvfrom(UDP_BUFSIZE)
        if not data:
            break
        rec_msg = data.decode("utf-8")
        print("server rec:", rec_msg)
        # 输出addr，是因为可以同时接收多个客户端的消息并发送回复消息，这样的输出有助于指示消息是从哪个客户端发送的
        msg = "server replay: {}, to {}".format(rec_msg, addr)
        udp_socket.sendto(bytes(msg, "utf-8"), addr)
    udp_socket.close()


if __name__ == '__main__':
    run()
