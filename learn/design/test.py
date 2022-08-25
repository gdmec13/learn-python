# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod


class People(ABC):

    @abstractmethod
    def eat(self):
        pass


class Fruit(ABC):

    @abstractmethod
    def get_name(self):
        pass


if __name__ == '__main__':
    pass
