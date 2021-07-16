import pytest
from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_opening_and_closing_mathces():
    actual = validate_brackets("()")
    expected = True
    assert actual == expected

def test_opening_and_closing_does_not_match():
    actual = validate_brackets("{]")
    expected = False
    assert actual == expected

def test_opening_and_closing_mixed_within_strings_match():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected

def test_with_extra_opening_or_closing():
    actual = validate_brackets("()]")
    expected = False
    assert actual == expected
