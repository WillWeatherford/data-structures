# -*- coding: utf-8 -*-
u"""
Takes a string as input and returns one of three possible values.

Return 1 if the string is "open" (there are open parens that are not closed)
Return 0 if the string is "balanced" (there are an equal number of open and
    closed parentheses in the string)
Return -1 if the string is “broken” (a closing parens has not been proceeded
    by one that opens)
"""


def proper_parens(string):
    """Return -1, 0 or 1, depending on parens balance in given string."""
    count = 0
    for char in string:
        count += char == '('
        count -= char == ')'
        if count < 0:
            return -1
    return int(count > 0)
