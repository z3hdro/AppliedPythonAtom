#!/usr/bin/env python
# coding: utf-8

import pytest
import gzip

from lectures.lecture_01.scripts.submission import calculator


@pytest.fixture
def load_test_data():
    import os
    testname = os.path.basename(__file__)
    testname = os.path.splitext(testname)[0]
    with gzip.open(os.path.join("tests/tests_data",
                                testname + ".tar.gz"), 'rb') as f:
        output = f.read()
    return output


def test_calculator(load_test_data):
    params = load_test_data
    for arguments, result in params:
        x = int(arguments[0])
        y = int(arguments[1])
        operation = arguments[2]
        assert calculator(x, y, operation) == int(result)
