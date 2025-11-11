import pytest
from math_ops import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    def helper(x, y):
        assert divide(x, y) * y == x
    helper(10, 2)
    helper(9, 3)

class TestAdvancedMath:
    def test_negative(self):
        assert add(-5, -5) == -10
