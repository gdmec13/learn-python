# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, NewType


class Subject(ABC):

    @abstractmethod
    def add(self, observer: Observer):
        pass

    @abstractmethod
    def remove(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject):
        pass


class ConcreteSubject(Subject):

    _state: int = None

    _observer_list: List[Observer] = []

    def add(self, observer: Observer):
        self._observer_list.append(observer)

    def remove(self, observer: Observer):
        self._observer_list.remove(observer)

    def send_msg_logic(self, s):
        print("发消息来了:", s)
        self.notify()

    def notify(self):
        for ob in self._observer_list:
            ob.update(self)


class ExampleA(Observer):
    def update(self, subject: Subject):
        print("xxxxxxExampleA", subject._state)


class ExampleB(Observer):
    def update(self, subject: Subject):
        print("xxxxxxExampleA", subject._state)


if __name__ == '__main__':
    subject = ConcreteSubject()

    a = ExampleA()
    subject.add(a)
    a.update(subject)

    b = ExampleB()
    subject.add(b)
    b.update(subject)

    subject.send_msg_logic("are you ok?")

    subject.remove(a)

    subject.send_msg_logic("today is nice")




