# -*- coding: utf-8 -*-
from concurrent import futures
import logging
import grpc

# 引入自动生成的代码
import tester_pb2
import tester_pb2_grpc


# 继承tester_pb2_grpc中的TesterServicer接口，并实现proto中的两个方法
class TesterServicer(tester_pb2_grpc.TesterServicer):
    def Add(self, request, context):
        # 初始化NumberResult类型返回值
        response = tester_pb2.NumberResult()
        # request是NumberPair类型，因此有num1和num2两个变量
        print('Add(%d, %d) is called' % (request.num1, request.num2))
        response.value = request.num1 + request.num2
        return response

    def Merge(self, request, context):
        # 初始化StringResult类型返回值
        response = tester_pb2.StringResult()
        # request是StringPair类型，因此有str1和str2两个变量
        print('Merge(%s, %s) is called' % (request.str1, request.str2))
        response.value = request.str1 + request.str2
        return response


def serve():
    # 创建RPC Server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册RPC调用方法
    tester_pb2_grpc.add_TesterServicer_to_server(TesterServicer(), server)
    server.add_insecure_port('[::]:50051')  # 监听50051端口
    server.start()  # 启动Server
    print('Server Starting...')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
