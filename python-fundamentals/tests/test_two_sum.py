import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from arrays.two_sum import two_sum


def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 100) == []


def test_two_sum_negative_numbers():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
