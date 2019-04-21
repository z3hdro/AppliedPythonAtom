#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """
    sm = np.sum((y_true * np.log(y_pred)) + (1 - y_true) * np.log(1 - y_pred))
    return -1 * (sm / len(y_true))


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    m = []
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            m.append(1)
    return len(m) / len(y_true)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    m = []
    for i in range(len(y_true)):
        if (y_pred[i] == 1) and (y_true[i] == 1):
            m.append(1)
    full = np.count_nonzero(y_pred)
    return len(m) / full


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    m = []
    for i in range(len(y_true)):
        if (y_pred[i] == 1) and (y_true[i] == 1):
            m.append(1)
    full = np.count_nonzero(y_true)
    return len(m) / full


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """

    t = []
    k = []
    ones = []
    zeros = []
    result = []
    step = 1 / len(y_true)
    m = 0
    while m <= 1:
        t.append(m)
        m += step
    for l in t:
        for j in range(len(y_pred)):
            if y_pred[j] > l:
                k.append(1)
            else:
                k.append(0)
        y_hat = np.array(k)
        for i in range(len(y_true)):
            if (y_hat[i] == 1) and (y_true[i] == 1):
                ones.append(1)
        ones_length = np.count_nonzero(y_true)
        TPR = len(ones) / ones_length
        for i in range(len(y_true)):
            if (y_hat[i] == 0) and (y_true[i] == 0):
                zeros.append(0)
        zeros_length = len(y_hat) - ones_length
        FPR = 1 - (len(zeros) / zeros_length)
        answer = (1 + TPR - FPR) / 2
        result.append(answer)
        k.clear()
        ones.clear()
        zeros.clear()
    return max(result)
