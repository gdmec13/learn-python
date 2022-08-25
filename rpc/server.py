# -*- coding: utf-8 -*-
import reco_pb2
import reco_pb2_grpc
import grpc
from concurrent.futures import ThreadPoolExecutor
import time


class UserRecommendService(reco_pb2_grpc.UserRecommendServicer):

    def user_commend(self, request, context):
        user_id = request.user_id
        channel_id = request.channel_id
        article_num = request.article_num
        time_stamp = request.time_stamp

        response = reco_pb2.ArticleResponse()
        response.exposure = 'exposure param'
        response.time_stamp = round(time.time() * 1000)
        recommends = []
        for i in range(article_num):
            article = reco_pb2.Article()
            article.track.click = 'click param {}'.format(i+1)
            article.track.collect = 'collect param {}'.format(i+1)
            article.track.share = 'share param {}'.format(i+1)
            article.track.read = 'read param {}'.format(i+1)
            article.article_id = i+1
            recommends.append(article)
        response.recommends.extend(recommends)

        return response


def serve():
    """
    rpc 服务端启动方法
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    reco_pb2_grpc.add_UserRecommendServicer_to_server(UserRecommendService(), server)

    server.add_insecure_port('127.0.0.1:8866')

    server.start()
    print("running....")

    # start() 不会阻塞，此处需要加上循环睡眠，防止程序退出
    while True:
        time.sleep(10)


if __name__ == '__main__':
    serve()
