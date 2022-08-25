# -*- coding: utf-8 -*-
from socket import *
from time import ctime

"""
创建tcp服务器：伪代码
ss = socket() # 创建服务器套接字
ss.bind() # 套接字与地址绑定
ss.listen() # 监听连接
inf_loop: # 服务器无限循环
 cs = ss.accept() # 接受客户端连接
 comm_loop: # 通信循环
 cs.recv()/cs.send() # 对话（接收/发送）
 cs.close() # 关闭客户端套接字
ss.close() # 关闭服务器套接字#（可选）
"""


HOST = 'localhost'
PORT = 12451
# 缓冲区大小设置为 1KB, 可以根据网络性能和程序需要改变这个容量
BUFSIZE = 1024
ADDR = (HOST, PORT)


def run():
    # 创建 TCP/IP 套接字
    tcp_ser_sock = socket(AF_INET, SOCK_STREAM)
    # 将地址（主机名、端口号对）绑定到套接字上
    tcp_ser_sock.bind(ADDR)

    # 设置并启动 TCP 监听器，被动接受 TCP 客户端连接，一直等待直到连接到达（阻塞）
    # 参数：在连接被转接或拒绝之前，传入连接请求的最大数
    tcp_ser_sock.listen(5)

    try:
        while True:
            print("waiting for connection ...")
            # 被动接受 TCP 客户端连接，一直等待直到连接到达（阻塞）
            tcp_cli_sock, addr = tcp_ser_sock.accept()
            print("... connected from : {}".format(addr))

            while True:
                # 接收 TCP 消息
                data = tcp_cli_sock.recv(BUFSIZE)
                print("recv:", data, type(data))
                if not data:
                    break
                # 发送 TCP 消息
                tcp_cli_sock.send(bytes('[ %s ] %s' % (ctime(), data), "utf-8"))
            tcp_cli_sock.close()
    except KeyboardInterrupt as e:
        tcp_ser_sock.close()
        print(e)
    except EOFError as e:
        tcp_ser_sock.close()
        print(e)


if __name__ == '__main__':
    run()

