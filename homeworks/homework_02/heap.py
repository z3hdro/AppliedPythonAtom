#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        pass

    def add(self, elem_with_priority):
        pass

    def build_heap(self):
        pass


class MaxHeap(Heap):

    def __init__(self, array):
        raise NotImplementedError

    def extract_maximum(self):
        pass


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
