#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):

    """
    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    answer = np.array([])
    e = np.eye(len(a) + 1)
    b1 = np.hstack((b, (np.zeros(1)))).reshape(1, (len(a) + 1)).transpose()
    md = np.hstack(((np.vstack((a, (-1*c))), e)))
    sm = np.hstack((md, b1))
    while (np.min(sm[-1, :-1])) < 0:
        index_c = np.transpose(np.nonzero(sm == np.min(sm[-1, :-1])))
        column_index = index_c[-1][1]
        pivot_column = sm[:, column_index]
        pivot_m = np.array([pivot_column, ]*((sm.shape)[1])).transpose()
        sm1 = sm/pivot_m
        min_pivot = np.min(sm1[:-1, -1])
        index_r = np.transpose(np.nonzero(sm1 == min_pivot))
        if len(index_r) == 1:
            row_index = index_r[0][0]
        else:
            row_index = index_r[-1]
        pivot = sm[row_index, column_index]
        pivot_row = (sm[row_index])/pivot
        sm[row_index] = pivot_row
        for i in range((sm.shape)[0]):
            if i == row_index:
                continue
            sm[i] = sm[i] - pivot_row * sm[i, column_index]
    for i in range((a.shape)[1]):
        if (np.linalg.norm(sm[:, i]) == 1) & (len(np.nonzero(sm[:, i])[0]) == 1):
            answer = np.append(answer, sm[np.nonzero(sm[:, i])[0], -1])
        else:
            answer = np.append(answer, [0])
    return answer
