# coding: utf-8
# license: GPLv3
from gameunit import *


class Hero(Attacker):
    _name = ''
    _experience = 0

    def __init__(self, new_name):
        self._attack = 50
        self._health = 100
        self._name = new_name


    #def attack(self, target):
        #target._health -= self.attack()


    #FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
