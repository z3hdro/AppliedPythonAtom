#!/usr/bin/env python
# coding: utf-8


class Heap:

    def __init__(self, array):
        self.heap = array[:]
        self.build_heap()

    def siftup(self, index: int):
        arr = self.heap
        parent = (index - 1) // 2
        while index > 0 and comparator_d(arr[index], arr[parent]):
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
            parent = (index - 1) // 2

    def siftdown(self, i: int):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.heap) and \
                comparator_d(self.heap[left], self.heap[largest]):
            largest = left

        if right < len(self.heap) and \
                comparator_d(self.heap[right], self.heap[largest]):
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.siftdown(largest)

    def add(self, elem_with_priority):
        self.heap.append(elem_with_priority)
        self.siftup(len(self.heap) - 1)

    def build_heap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self.siftdown(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.siftdown(0)
        return maximum


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
