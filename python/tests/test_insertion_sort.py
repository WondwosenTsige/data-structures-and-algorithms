import pytest
from python.code_challenges.merge_sort.merge_sort import insertion_sort


def test_empty_list():
    list = []
    actual = insertion_sort(list)
    expected = 'List is empty. Nothing to sort'
    assert actual == expected
