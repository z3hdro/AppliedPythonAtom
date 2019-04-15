#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if y_true.shape == y_hat.shape:
            return (np.sum((y_true - y_hat) ** 2) / len(y_true))


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if y_true.shape == y_hat.shape:
        return (np.sum(np.abs(y_true - y_hat)) / len(y_true))


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if y_true.shape == y_hat.shape:
        y_true_average = np.average(y_true)
        y_mse = (np.sum((y_true - y_hat) ** 2) / len(y_true))
        y_mse_average = (np.sum((y_true - y_true_average) ** 2) / len(y_true))
        return 1 - y_mse/y_mse_average
