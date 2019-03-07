#!/usr/bin/env python
# coding: utf-8

import os

from utils.file_processors import PickleFileProcessor

from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.vkposter import VKPoster
from homeworks.homework_02.fastmerger import FastSortedListMerger


def load_test_data(func_name):
    file_processor = PickleFileProcessor()
    test_filename = os.path.basename(__file__)
    test_filename = os.path.splitext(test_filename)[0]
    test_filename = os.path.join("tests/tests_data",
                                 test_filename + "_" + func_name + ".ini.pkl")
    output = file_processor.read_file(test_filename)
    return output


def test_max_heap():
    try:
        h = MaxHeap([])
    except NotImplementedError:
        return True

    import random
    random.seed(121212)
    # заведем макс кучу
    some_list = [(random.randint(10, 20), 'setup') for i in range(7)]
    h = MaxHeap(some_list)
    # добавим элементов с разным приоритетом
    some_list_2 = [(random.randint(-20, 40), 'setup') for i in range(9)]
    [h.add(i) for i in some_list_2]
    merged_list = some_list + some_list_2
    # проверим что всегда макс элемент это макс элемент
    sorted_merged_list = sorted(merged_list, key=lambda x: x[0], reverse=True)
    for i, next_max in enumerate(sorted_merged_list):
        max_ = h.extract_maximum()
        assert max_ == next_max, 'heap - element {} {}'.format(max_, next_max)
    some_list = [(random.randint(0, 20), '9999') for i in range(13)]
    h = MaxHeap(some_list)
    # Проверим что макс куча всегда правильно вытаскивает максимум.
    for next_max in sorted(some_list, key=lambda x: x[0], reverse=True):
        max_ = h.extract_maximum()
        assert max_ == next_max, 'heap - element {} {}'.format(max_, next_max)
    return True


def test_fastmerger():
    data = load_test_data("fastmerger")
    try:
        FastSortedListMerger.merge_first_k([[1, 2, 3], [3, 4, 5]], 4)
        # should return [5,4,3,3]
    except NotImplementedError:
        return True
    for case in data:
        assert FastSortedListMerger.merge_first_k(
            *case['params']) == case['ans']
    return True


def test_vk_poster():
    data = load_test_data("vk_poster")
    try:
        vk_poster = VKPoster()
    except NotImplementedError:
        return True
    for test in data:
        vk_poster = VKPoster()
        for action, params, ans in zip(
                test['action'], test['params'], test['expected_ans']):
            if action == 'follow':
                assert ans == vk_poster.user_follow_for(*params)
            elif action == 'posted':
                assert ans == vk_poster.user_posted_post(*params)
            elif action == 'get_recent_posts':
                assert ans == vk_poster.get_recent_posts(*params)
            elif action == 'readed':
                assert ans == vk_poster.user_read_post(*params)
            elif action == 'get_most_popular_posts':
                assert ans == vk_poster.get_most_popular_posts(*params)
    return True
