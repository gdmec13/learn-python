# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def test_func(self):
        pass


class Test(AbstractFactory):
    def create_product_a(self):
        print("hello world!")

    def test_func(self):
        print("welcome to the company!")


if __name__ == "__main__":
    cls = Test()
    cls.create_product_a()
    cls.test_func()

