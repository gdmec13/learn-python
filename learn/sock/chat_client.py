# -*- coding: utf-8 -*-
from socket import *
from config import Config
from multiprocessing import Process
from chat_ser import TcpServer


def tcp_client():
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(Config.ADDRESS_TOUPLE)
    first_res = tcp_client_socket.recv(Config.BUFSIZE)
    if first_res:
        print(first_res.decode("utf-8"))

    while True:
        msg = input("> ")
        if not msg:
            break
        msg = bytes(msg, "utf-8")
        tcp_client_socket.send(msg)
        recv_data = tcp_client_socket.recv(Config.BUFSIZE)
        if not recv_data:
            break
        print("server result:", recv_data.decode("utf-8"))
    tcp_client_socket.close()
    return True


def run(m):
    if m not in ['1', '0']:
        print("please choose true model")
    else:
        if m == '1':
            print("server starting...")
            # 尝试服务端丢到进程中，服务端那边用文本来做回复等
            p = Process(target=TcpServer.run, args=())
            p.start()
            print("client starting...")
            tcp_client()
            # 客户端退出时，服务端也不用跑了。
            p.kill()
        else:
            print("exit success")
            exit()


if __name__ == '__main__':
    print("-------------------------------")
    print("welcome to chat, now you can choose model")
    print("[1-into chat] [0-exit]")
    print("-------------------------------")

    input_model = input('please input model >')
    run(input_model)
