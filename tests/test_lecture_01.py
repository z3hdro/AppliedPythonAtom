#!/usr/bin/env python
# coding: utf-8

import pytest

from lectures.lecture_01.scripts.submission import calculator


@pytest.fixture
def load_test_data():
    import os
    output = []
    with open(os.path.join("tests_data", os.path.splitext(os.path.basename(__file__))[0] + ".ini")) as fin:
        for line in fin:
            output.append((line.split()[:-1], line.split()[-1]))
    return output


def test_calculator(load_test_data):
    params = load_test_data
    for arguments, result in params:
        assert calculator(int(arguments[0]), int(arguments[1]), arguments[2]) == int(result)

