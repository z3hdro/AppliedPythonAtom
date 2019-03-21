#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.array = array[:]
        self.comparator = None

    def _shift_down(self, i):
        # помогаем "утопить" неугодный элемент
        # если макс куча - то топим минимум
        # если мин куча - то топим максимум
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        heap_size = len(self.array) - 1
        if left <= heap_size and self.comparator(self.array[left], self.array[largest]):
            largest = left
        if right <= heap_size and self.comparator(self.array[right], self.array[largest]):
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self._shift_down(largest)
            # _shift_down для потомка с новым значением
            # получается опускаем вниз элемент-родитель
            # и снова сравниваем его уже с новыми потомками

    def _shift_up(self, i):
        # помогаем всплыть элементу
        parent = (i - 1) // 2
        while i > 0 and self.comparator(self.array[i], self.array[parent]):
            self.array[parent], self.array[i] = self.array[i], self.array[parent]
            i = parent
            parent = (i - 1) // 2

    def add(self, elem_with_priority):
        # добавляем новый элемент.
        # лучше добавить в конец (как лист)
        # и поднимать его
        self.array.append(elem_with_priority)
        self._shift_up(len(self.array) - 1)

    def build_heap(self):
        heap_size = len(self.array) - 1
        for i in range(0, heap_size // 2 + 1)[::-1]:
            self._shift_down(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)
        self.comparator = comparator_d
        self.build_heap()

    def extract_maximum(self):
        if len(self.array) > 0:
            res = self.array[0]
            self.array[0] = self.array[-1]
            del self.array[-1]
            self._shift_down(0)
            return res


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
