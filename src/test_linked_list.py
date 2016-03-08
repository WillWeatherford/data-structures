# # -*- coding: utf-8 -*-
import pytest


TEST_LST = [
    ([1, 2, 3], (3, 2, 1)),
    ('abc', ('c', 'b', 'a')),
    ([7, 8, 9], (9, 8, 7)),
    (range(100), tuple(reversed(range(100)))),
]

SIZE_TEST = [
    ([0, 1, 2], 3),
    ([], 0),
    ('abcdefg', 7),
    ((0, 0, 'astring', 8, []), 5),
    (range(100), 100),
]

INSERT_TEST = [
    ([0, 1, 2], 'a'),
    ('abcdefg', 1),
    ((0, 0, 'astring', 8, []), 0),
    ([], []),
]


POP_TEST = [
    ([0, 1, 2], 2, 1),
    ([], None, None),
    ('abcdefg', 'g', 'f'),
    ((0, 0, 'astring', 8, []), [], 8),
    (range(100), 99, 98),
]


@pytest.mark.parametrize('seq, result', TEST_LST)
def test_init(seq, result):
    from linked_list import Linked_List
    instance = Linked_List(seq)
    assert instance.head[0] == seq[-1]


@pytest.mark.parametrize('seq, result', TEST_LST)
def test_display(seq, result):
    from linked_list import Linked_List
    instance = Linked_List(seq)
    assert instance.display() == result


@pytest.mark.parametrize('seq, val', INSERT_TEST)
def test_insert(seq, val):
    from linked_list import Linked_List
    instance = Linked_List(seq)
    instance.insert(val)
    assert instance.head[0] == val


@pytest.mark.parametrize('seq, popped_val, new_head', POP_TEST)
def test_pop(seq, popped_val, new_head):
    from linked_list import Linked_List
    instance = Linked_List(seq)
    assert instance.pop() == popped_val
    assert instance.size() == max([len(seq) - 1, 0])
