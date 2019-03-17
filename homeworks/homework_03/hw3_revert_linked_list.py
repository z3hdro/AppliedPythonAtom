#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    if not head:
        return None
    after = None
    before = None
    while head:
        after = head.next_node
        head.next_node = before
        before = head
        head = after
    return before
