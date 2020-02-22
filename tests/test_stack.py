import pytest

from ds.stack import Stack


def test_push_over_size():
    stack = Stack()
    with pytest.raises(AssertionError):
        for i in range(0, 11):
            stack.push(i)


def test_push():
    stack = Stack()
    for i in range(0, 10):
        stack.push(i)


def test_pop():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
