#!/usr/bin/env python
# coding: utf-8
import re


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    try:
        x = re.findall("[0-9]", input_string)
        if len(x) == 0:
            return None
        if "**" in input_string:
            return None
        for elm in input_string:
            if elm.isalpha() or "," in elm:
                return None
            if "[" in elm or "]" in elm:
                return None
        return eval(input_string)
    except SyntaxError:
        return None
