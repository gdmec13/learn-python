# -*- coding: utf-8 -*-
"""
c = Animal()
c.run("狗")
c.fly("狗")
c.swim("狗")
"""
class Animal(object):

    def run(self, name):
        print("{}：在陆地上跑起来了".format(name))

    def fly(self, name):
        print("{}：在空中飞起来了".format(name))

    def swim(self, name):
        print("{}：在水里游起来了".format(name))


class LandAnimal(object):
    @classmethod
    def run(cls, name):
        print("{}：在陆地上跑起来了".format(name))

    def business_logic(self):
        """
        业务逻辑拓展
        """
        pass


class AirAnimal(object):
    @classmethod
    def run(cls, name):
        print("{}：在空中飞起来了".format(name))


class WaterAnimal(object):
    @classmethod
    def run(cls, name):
        print("{}：在水里游起来了".format(name))


if __name__ == '__main__':
    LandAnimal.run("狗")
    AirAnimal.run("麻雀")
    WaterAnimal.run("小鱼")
