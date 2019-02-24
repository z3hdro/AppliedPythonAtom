#!/usr/bin/env python
# coding: utf-8

import pytest

from lectures.lecture_01.scripts.submission import calculator


@pytest.fixture
def load_test_data():
    import os
    output = []
    testname = os.path.basename(__file__)
    testname = os.path.splitext(testname)[0]
    with open(os.path.join("tests/tests_data",
                           testname + ".ini")) as fin:
        for line in fin:
            output.append((line.split()[:-1], line.split()[-1]))
    return output


def test_calculator(load_test_data):
    params = load_test_data
    for arguments, result in params:
        x = int(arguments[0])
        y = int(arguments[1])
        operation = arguments[2]
        assert calculator(x, y, operation) == int(result)
