#!/usr/bin/env python
# coding: utf-8

import numpy as np


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self.th = None
        self.left = None
        self.right = None

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        m = []
        sort = X.argsort()
        X = X[0, sort[0]]
        y = y[0, sort[0]]
        idx = np.argmin([(np.var(y[:i]) * i + np.var(y[i:]) * (y.shape[0] - i)) / y.shape[0]
                         for i in range(1, X.shape[0])])
        self.th = X[idx]
        self.left = np.mean(y[:idx])
        self.right = np.mean(y[idx:])

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        res = []
        for i in X:
            if i > self.th:
                res.append(self.right)
            else:
                res.append(self.left)
        return np.array(res)
