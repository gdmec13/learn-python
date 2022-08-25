# -*- coding: utf-8 -*-
from __future__ import print_function
import logging
import grpc

# 引入自动生成的代码
import tester_pb2
import tester_pb2_grpc


def run():
    # 通过本地端口50051建立通道
    with grpc.insecure_channel('localhost:50051') as channel:
        # 获取RPC调用的代理类
        stub = tester_pb2_grpc.TesterStub(channel)
        response = stub.Add(tester_pb2.NumberPair(num1=3, num2=4))  # 调用Add方法
        print("3 + 4 = %d" % response.value)  # response是NumberResult类型，因此有一个value变量
        response = stub.Merge(tester_pb2.StringPair(str1='Hello ', str2='Python'))  # 调用Merge方法
        print("Hello + Python = %s" % response.value)  # response是StringResult类型，因此有一个value变量


if __name__ == '__main__':
    logging.basicConfig()
    run()
