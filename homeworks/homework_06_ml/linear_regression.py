#!/usr/bin/env python
# coding: utf-8
import numpy as np
from sklearn.metrics import mean_squared_error


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_coef = lambda_coef
        self.regulatization = regulatization
        self.alpha = alpha

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        iterations = 10000
        accuracy = 0.001
        X_const = np.hstack(((np.ones((X_train.shape[0], 1))),X_train))
        D = X_const.shape[1]
        self.w = (np.random.randn(D)).reshape(-1, 1)
        row = self.w.shape[0]
        N = y_train.shape[0]
        if N == ((X_const @ self.w).shape[1]):
            if self.regulatization == 'L2':
                weight = self.alpha * np.sum(self.w[1:, 0] ** 2)
            elif self.regulatization == 'L1':
                weight = self.alpha * np.sum(np.abs(self.w[1:, 0]))
            else:
                weight = 0
            for i in range(iterations):
                self.loss = mean_squared_error(y_train, (X_const @ self.w)) + weight
                if self.loss > accuracy:
                    if self.regulatization == 'L2':
                        derivative = self.alpha * np.ones((D, 1)) / 2
                    elif self.regulatization == 'L1':
                        derivative = self.alpha * self.w
                    else:
                        derivative = 0
                    self.w -= (-2) * self.lambda_coef * X_const.T @ (y_train - (X_const @ self.w)) + derivative
                else:
                    break
                    

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        return (np.hstack(((np.ones((X_test.shape[0], 1))),X_test))).dot(self.w)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.w
