#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        arr = [i[:] for i in list_of_lists]
        heap = MaxHeap([(j.pop(), i) for i, j in enumerate(arr)
                       if len(j) > 0])
        result = []
        for i in range(k):
            try:
                inner = heap.extract_maximum()
            except IndexError:
                return result
            result.append(inner[0])
            if len(arr[inner[1]]) > 0:
                heap.add((arr[inner[1]].pop(), inner[1]))
        return result
