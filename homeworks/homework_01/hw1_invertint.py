#!/usr/bin/env python
# coding: utf-8


def reverse(number):
   
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
     if number >= 0:
        flag = 0
    else:
        flag = 1
    x = str(number)
    if flag is 0:
        y = x[::-1]
        z = int(y)
        return z
    else:
        y = x[1:]
        v = y[::-1]
        z = int(v)
        return -1 * z
