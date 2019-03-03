#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    new_dict = {}
    for key, value in source_dict.items():
        for i in range(0, len(value), 1):
            if not (value[i] in new_dict):
                new_dict[value[i]] = key
            elif new_dict[value[i]] is list() or tuple():
                new_dict[value[i]].append(key)
            elif new_dict[value[i]] is set():
                new_dict[value[i]].add(key)
            else:
                new_dict[value[i]] = [new_dict[value[i]]]
                new_dict[value[i]].append(key)
    return new_dict