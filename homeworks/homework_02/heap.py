#!/usr/bin/env python
# coding: utf-8


class Heap:

    def __init__(self, array):
        self.heap = array[:]
        self.build_heap()

    def siftup(self, index: int):
        parent = (index - 1) // 2
        arr = self.heap
        while index > 0 and comparator_d(arr[index], arr[parent]):
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
            parent = (index - 1) // 2

    def siftdown(self, i: int):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        while True:
            if left < len(self.heap) and \
                    comparator_d(self.heap[left], self.heap[largest]):
                largest = left

            if right < len(self.heap) and \
                    comparator_d(self.heap[right], self.heap[largest]):
                largest = right
            if largest == i:
                break
                
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i.largest

    def add(self, elem_with_priority):
        self.heap.append(elem_with_priority)
        self.siftup(len(self.heap) - 1)

    def build_heap(self):
        for i in range(len(self.heap)//2, -1, -1):
            self.siftdown(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        maximum = self.heap.pop(0)
        self.build_heap()
        return maximum


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
