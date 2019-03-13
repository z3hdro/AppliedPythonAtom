#!/usr/bin/env python
# coding: utf-8

import random

from homeworks.homework_03.hw3_hashmap import HashMap
from homeworks.homework_03.hw3_hashset import HashSet
from homeworks.homework_03.hw3_lrucache import LRUCacheDecorator
from homeworks.homework_03.hw3_testing import MockOrdinaryFileWorker


def test_hashmap_01():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        assert hashmap._get_hash(k) == hash(k)
        assert hashmap._get_hash(v) == hash(v)
    for k, v in entries:
        assert hashmap._get_index(hashmap._get_hash(k)) == hash(k) % 10
        assert hashmap._get_index(hashmap._get_hash(v)) == hash(v) % 10


def test_hashmap_02():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        assert k in hashmap


def test_hashmap_03():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    inner_list_name = [k for k, v in hashmap.__dict__.items() if isinstance(v, list)][0]
    for k, v in entries:
        hashmap.put(k, v)
    for k, v in entries:
        assert HashMap.Entry(k, None) in hashmap.__dict__[inner_list_name][hashmap._get_index(hashmap._get_hash(k))]


def test_hashmap_04():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ()), ({"s": "v"}, {"v": "s"})]
    for k, v in entries:
        entry = HashMap.Entry(k, v)
        assert entry.get_key() == k
        assert entry.get_value() == v

    for i in range(len(entries)):
        entry_one = HashMap.Entry(entries[i][0], entries[i][1])
        for _ in range(10):
            j = random.randint(0, len(entries) - 1)
            p = random.randint(0, len(entries) - 1)
            entry_two = HashMap.Entry(entries[j][0], entries[p][1])
            if j == i:
                assert entry_one == entry_two
            else:
                assert entry_one != entry_two


def test_hashmap_05():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    for k, v in entries:
        assert hashmap.get(k) == v
    for _ in range(100):
        i = random.randint(0, len(entries) - 1)
        j = random.randint(0, len(entries) - 1)
        hashmap.put(i, j)
        assert hashmap.get(i) == j
    assert hashmap.get("nexit", "default") == "default"


def test_hashmap_06():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    output_values = set()
    output_keys = set()
    for v in hashmap.values():
        output_values.add(v)
    for k in hashmap.keys():
        output_keys.add(k)
    for k, v in entries:
        assert k in output_keys
        assert v in output_values
    output_values = set()
    output_keys = set()
    for k, v in hashmap.items():
        output_values.add(v)
        output_keys.add(k)
    for k, v in entries:
        assert k in output_keys
        assert v in output_values


def test_hashmap_07():
    try:
        hashmap = HashMap(2)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        assert k in hashmap
