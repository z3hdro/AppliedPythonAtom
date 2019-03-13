#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''
    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''

        def get_key(self):
            #py TODO возвращаем ключ

        def get_value(self):
            # TODO возвращаем значение

        def __eq__(self, other):
            # TODO реализовать функцию сравнения

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''

    def get(self, key, default_value=None):
        #TODO метод get, возвращающий значение,
        # если оно присутствует, иначе default_value

    def put(self, key, value):
        #TODO метод put, кладет значение по ключу,
        # в случае, если ключ уже присутствует он его заменяет

    def __len__(self):
        # TODO Возвращает количество Entry в массиве

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве

    def values(self):
        # TODO Должен возвращать итератор значений

    def keys(self):
        # TODO Должен возвращать итератор ключей

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
