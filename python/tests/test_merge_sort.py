from python.code_challenges.merge_sort.merge_sort import merge_sort
import pytest
from code_challenges.merge_sort import *

# @pytest.mark.skip("pending")
def test_empty_list():
    list = []
    actual = merge_sort(list)
    expected = 'List is empty. Nothing to sort'
    assert actual == expected
