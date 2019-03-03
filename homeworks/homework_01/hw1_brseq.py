#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    s = input_string
    while "[]" in s or "()" in s or "{}" in s:
        s = s.replace("[]", "")
        s = s.replace("()", "")
        s = s.replace("{}", "")
    if s == "":
        return True
    else:
        return False
