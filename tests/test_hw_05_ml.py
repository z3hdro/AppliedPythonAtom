#!/usr/bin/env python
# coding: utf-8


import numpy as np
from homeworks.homework_05_ml.simplex_method import simplex_method
from homeworks.homework_05_ml.csr_matrix import CSRMatrix


def test_simplex_method_01():
    a = np.array([[2, 3, 2], [1, 1, 2]])
    b = np.array([1000, 800])
    c = np.array([7, 8, 10])

    true_x = np.array([200, 0, 300])

    try:
        x = simplex_method(a, b, c)
    except NotImplementedError:
        return True

    assert len(true_x) == len(x)
    assert all(np.isclose(x[i], true_x[i]) for i in range(len(x)))


def test_simplex_method_02():
    a = np.array([[6, 3, 1, 4], [2, 4, 5, 1], [1, 2, 4, 3]])
    b = np.array([252, 144, 80])
    c = np.array([48, 33, 16, 22])

    true_x = np.array([32, 20, 0, 0])

    try:
        x = simplex_method(a, b, c)
    except NotImplementedError:
        return True

    assert len(true_x) == len(x)
    assert all(np.isclose(x[i], true_x[i]) for i in range(len(x)))


def test_simplex_method_03():
    a = np.array([[2, 3, 6], [4, 2, 4], [4, 6, 8]])
    b = np.array([240, 200, 160])
    c = np.array([4, 5, 4])

    true_x = np.array([40, 0, 0])

    try:
        x = simplex_method(a, b, c)
    except NotImplementedError:
        return True

    assert len(true_x) == len(x)
    assert all(np.isclose(x[i], true_x[i]) for i in range(len(x)))


def test_simplex_method_04():
    a = np.array([[12, 3], [4, 5], [3, 14]])
    b = np.array([264, 136, 266])
    c = np.array([6, 4])

    true_x = np.array([19, 12])

    try:
        x = simplex_method(a, b, c)
    except NotImplementedError:
        return True

    assert len(true_x) == len(x)
    assert all(np.isclose(x[i], true_x[i]) for i in range(len(x)))


def test_simplex_method_05():
    a = np.array([[1, 2], [3, 3], [3, 1]])
    b = np.array([32, 60, 50])
    c = np.array([4, 2])

    true_x = np.array([15, 5])

    try:
        x = simplex_method(a, b, c)
    except NotImplementedError:
        return True

    assert len(true_x) == len(x)
    assert all(np.isclose(x[i], true_x[i]) for i in range(len(x)))


def test_csr_matrix_init_from_data_row_col():
    np.random.seed(42)

    matrix = np.random.randint(0, 2, (200, 200))
    data = []
    row_ind = []
    col_ind = []
    for i, j in zip(range(matrix.shape[0]), range(matrix.shape[1])):
        data.append(matrix[i, j])
        row_ind.append(i)
        col_ind.append(j)

    try:
        csr_matrix = CSRMatrix((row_ind, col_ind, data))
    except NotImplementedError:
        return True

    for i, j in zip(range(matrix.shape[0]), range(matrix.shape[1])):
        assert np.isclose(matrix[i, j], csr_matrix.get_item(i, j))


def test_csr_matrix_get_item_method():
    np.random.seed(42)

    matrix = np.random.randint(0, 2, (200, 200))
    try:
        csr_matrix = CSRMatrix(matrix)
    except NotImplementedError:
        return True

    for i, j in zip(range(matrix.shape[0]), range(matrix.shape[1])):
        assert np.isclose(matrix[i, j], csr_matrix.get_item(i, j))


def test_csr_matrix_set_item_method():
    np.random.seed(42)

    zero_matrix = np.zeros((200, 200))
    matrix = np.random.randint(0, 3, (200, 200))
    try:
        csr_matrix = CSRMatrix(zero_matrix)
    except NotImplementedError:
        return True

    for i, j in zip(range(matrix.shape[0]), range(matrix.shape[1])):
        csr_matrix.set_item(i, j, matrix[i, j])

    for i, j in zip(range(matrix.shape[0]), range(matrix.shape[1])):
        assert np.isclose(matrix[i, j], csr_matrix.get_item(i, j))


def test_csr_matrix_03_to_dense_method():
    np.random.seed(42)

    matrix = np.random.randint(0, 2, (200, 200))
    try:
        csr_matrix = CSRMatrix(matrix)
    except NotImplementedError:
        return True

    dense_matrix = csr_matrix.to_dense()

    for i, j in zip(range(matrix.shape[0]), range(matrix.shape[1])):
        assert np.isclose(matrix[i, j], dense_matrix[i, j])
