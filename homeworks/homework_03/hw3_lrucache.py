#!/usr/bin/env python
# coding: utf-8

import time
from collections import OrderedDict


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        self.size = maxsize
        self.ttl = ttl
        self.cache = OrderedDict()
        self.origin = time.time()

    def __call__(self, func):
        # TODO вызов функции
        def wrapper(*args, **kwargs):
            col = set()
            for i in args:
                col.add(i)
            for key, value in kwargs.items():
                col.add(key)
                col.add(value)
            data = tuple(col)
            if self.ttl is None or time.time() - self.origin <= self.ttl:
                if data in self.cache:
                    if len(self.cache) == self.size:
                        temp = self.cache[data]
                        del self.cache[data]
                        self.cache[data] = temp
                    return self.cache[data]
                else:
                    if len(self.cache) == self.size:
                        del self.cache[list(self.cache.keys())[0]]
                    self.cache[data] = func(*args, **kwargs)
                    return func(*args, **kwargs)
            else:
                self.cache.clear()
                self.origin = time.time()
                self.cache[data] = func(*args, **kwargs)
                return func(*args, **kwargs)
        return wrapper
