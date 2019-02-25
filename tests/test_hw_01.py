#!/usr/bin/env python
# coding: utf-8

import os

from utils.file_processors import PickleFileProcessor
from homeworks.homework_01.hw1_calculator import calculator


def load_test_data(func_name):
    file_processor = PickleFileProcessor()
    test_filename = os.path.basename(__file__)
    test_filename = os.path.splitext(test_filename)[0]
    test_filename = os.path.join("tests/tests_data",
                                 test_filename + "_" + func_name + ".ini.pkl")
    output = file_processor.read_file(test_filename)
    return output


def test_calculator():
    data = load_test_data("calculator")
    try:
        calculator(1, 1, "plus")
    except NotImplementedError:
        return True
    for arguments in data:
        x = arguments[0]
        y = arguments[1]
        oper = arguments[2]
        result = arguments[3]
        if result is None:
            assert calculator(x, y, oper) is None
            continue
        output = abs(calculator(x, y, oper) - result)
        assert output / abs(result + 0.00001) < 0.005


def test_string_calculator():
    return True
