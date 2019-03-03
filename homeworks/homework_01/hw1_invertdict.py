#!/usr/bin/env python
# coding: utf-8


def inside(value):
    res = []
    if isinstance(value, (tuple, set, list)):
        for i in value:
            if isinstance(value, (tuple, set, list)):
                for j in inside(i):
                    res.append(j)
            else:
                res.append(i)
    else:
        res = [value]
    return res


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if type(source_dict) != dict:
        return source_dict
    new_dict = {}
    for pair in source_dict.items():
        for value in inside(pair[1]):
            if value not in new_dict:
                new_dict[value] = pair[0]
            elif type(new_dict[value]) is list:
                new_dict[value].append(pair[0])
            else:
                new_dict[value] = [new_dict[value]]
                new_dict[value].append(pair[0])
    return new_dict
