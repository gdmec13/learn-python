# -*- coding: utf-8 -*-
from socket import *
from config import Config
from time import ctime


def choose_res(msg):
    switch = {
        "hello": "hi",
        "what can i do for u?": 'go die please!'
    }
    return switch.get(msg, msg)


class TcpServer(object):

    @staticmethod
    def run():
        chat_tcp_socket = socket(AF_INET, SOCK_STREAM)
        chat_tcp_socket.bind(Config.ADDRESS_TOUPLE)
        chat_tcp_socket.listen(Config.LISTENT_NUM)

        while True:
            print("waiting connection ....")
            chat_socket, chat_addr = chat_tcp_socket.accept()
            chat_socket.send(bytes("server connect success, you can do it!", "utf-8"))

            while True:
                data = chat_socket.recv(Config.BUFSIZE)
                print("client send:", data.decode("utf-8"))
                if not data:
                    break
                msg = '[%s]: %s' % (ctime(), choose_res(data.decode("utf-8")))
                chat_socket.send(bytes(msg, "utf-8"))
            chat_socket.close()


if __name__ == '__main__':
    TcpServer.run()
