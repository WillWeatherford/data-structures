"""Test that proper_parens returns expected result."""

import pytest


STRINGS = [
    ('', 0),
    ('()', 0),
    ('()()()()(()()()()()()()()()()())', 0),
    ('(((f(((dss(((gg())644))`)[])yygwds))))', 0),

    ('(', 1),
    ('(()', 1),
    ('((( ) (( )))', 1),
    ('()()()()()(', 1),

    (')', -1),
    ('())', -1),
    (')))(((', -1),
    ('uhouh3lk(hsl)dfh)kasf', -1),
]


@pytest.mark.parametrize('string, result', STRINGS)
def test_proper_parens(string, result):
    """Test that proper_parens function returns expected result."""
    from proper_parens import proper_parens
    assert proper_parens(string) == result
