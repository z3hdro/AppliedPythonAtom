#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn.metrics import log_loss


class LogisticRegression:
    def __init__(self, n_iter=100, lambda_coef=1, accuracy=0.00001, regulatization=None, alpha=0.5):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.labmda_coef = lambda_coef
        self.regulatization = regulatization
        self.alpha = alpha
        self.n_iter = n_iter
        self.accuracy = accuracy

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        if not X_train.shape[0] == y_train.shape[0]:
            print('Different shapes')
        X_const = np.hstack(((np.ones((X_train.shape[0], 1))), X_train))
        n = X_const.shape[0]
        m = X_const.shape[1]
        self.w = np.random.randn(m).reshape(-1, 1)
        y_pred = (self.predict_proba(X_train)[:, 1]).reshape(-1, 1)
        init = log_loss(y_train, y_pred)
        for i in range(self.n_iter):
            if self.regularizarion == 'L2':
                derivative = 2 * self.alpha * self.w
                derivative[0] = 0
            elif self.regularizarion == 'L1':
                derivative = self.alpha * np.ones(m)
                derivative[0] = 0
            else:
                derivative = np.zeros(m)
            self.w -= -self.labmda_coef * (X_const.T @ (y_pred - y_train.reshape(-1, 1)) + derivative) / n
            y_pred = (self.predict_proba(X_train)[:, 1]).reshape(-1, 1)
            next = log_loss(y_train, y_pred)
            if np.abs(next - init) < self.accuracy:
                break
            init = next

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        X_test = np.hstack(((np.ones((X_test.shape[0], 1))), X_test))
        y_pred = 1 / (1 + np.exp(X_test @ self.w))
        return (y_pred > 0.5).astype('int64')

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        X_test = np.hstack(((np.ones((X_test.shape[0], 1))), X_test))
        y_test = 1 / (1 + np.exp(X_test @ self.w))
        return np.hstack((1 - y_test, y_test))

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.w
