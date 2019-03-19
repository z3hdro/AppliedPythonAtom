#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        return super().get(key)

    def put(self, key, value):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, value)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        super().__values()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        new_HashSet = HashSet()
        united_values = self.values() + another_hashset.values()
        for i in united_values:
            new_HashSet.put(i)
        return new_HashSet
