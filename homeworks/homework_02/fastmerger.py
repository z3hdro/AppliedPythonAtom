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
        result = []
        h = MaxHeap([(list_[-1], list_) for list_ in list_of_lists if len(list_) > 0])
        while len(result) < k and len(h.array) > 0:
            val, list_ = h.extract_maximum()
            list_.pop()
            if len(list_):
                h.add((list_[-1], list_))
            result.append(val)
        return result
