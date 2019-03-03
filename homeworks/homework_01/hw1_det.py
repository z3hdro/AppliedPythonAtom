#!/usr/bin/env python
# coding: utf-8


def min(matrix, j):
    return matrix[j][0], [row[1:] for row in matrix[:j] + matrix[j + 1:]]


def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    ans = 0
    for j in range(len(matrix)):
        A, M = min(matrix, j)
        ans += ((-1) ** j) * A * det(M)
    return ans


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    for i in list_of_lists:
        if len(i) != len(list_of_lists):
            return None
    return(det(list_of_lists))
