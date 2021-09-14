import pytest

from code_challenges.hashmpa_left_join.hashmap_left_join import left_join

def test_function_will_account_for_empty_left(hashmap1):
    actual = left_join({}, hashmap1)
    expected = []
    assert actual == expected


def test_function_will_account_for_empty_right(hashmap1):
    actual = left_join(hashmap1, {})
    expected = [["a", "aa", None], ["b", "bb", None], ["c", "cc", None], ["d", "dd", None], ["e", "ee", None]]
    assert actual == expected


def test_function_will_account_for_both_empty():
    actual = left_join({}, {})
    expected = []
    assert actual == expected


def test_function_will_account_for_all_matching():
    obj1 = {"a": "aa", "b": "bb", "c": "cc", "d": "dd", "e": "ee"}
    obj2 = {"a": "aa", "b": "bb", "c": "cc", "d": "dd", "e": "ee"}
    actual = left_join(obj1, obj2)
    expected = [["a", "aa", "aa"], ["b", "bb", "bb"], ["c", "cc", "cc"], ["d", "dd", "dd"], ["e", "ee", "ee"]]
    assert actual == expected


def test_function_will_account_for_left_side_larger():
    obj1 = {"a": "aa", "b": "bb", "c": "cc", "d": "dd", "e": "ee"}
    obj2 = {"c": "cc", "v": "vv", "e": "ee"}

    actual = left_join(obj1, obj2)
    expected = [["a", "aa", None], ["b", "bb", None], ["c", "cc", "cc"], ["d", "dd", None], ["e", "ee", "ee"]]
    assert actual == expected


def test_function_will_account_for_right_side_larger():
    obj1 = {"c": "cc", "v": "vv", "e": "ee"}
    obj2 = {"a": "aa", "b": "bb", "c": "cc", "d": "dd", "e": "ee"}
    actual = left_join(obj1, obj2)
    expected = [["c", "cc", "cc"], ["v", "vv", None], ["e", "ee", "ee"]]
    assert actual == expected


######################
# Fixtures
######################


@pytest.fixture
def hashmap1():
    obj = {"a": "aa", "b": "bb", "c": "cc", "d": "dd", "e": "ee"}
    return obj


@pytest.fixture
def hashmap2():
    obj = {"a": "aa", "b": "bb", "g": "gg", "h": "hh", "e": "ee"}
    return obj
