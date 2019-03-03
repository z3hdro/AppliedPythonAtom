#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    s = input_string
    while "[]" in s or "()" in s or "{}" in s:
        s = s.replace("[]", "")
        s = s.replace("()", "")
        s = s.replace("{}", "")
    if s != "":
        return False
    else:
        return True