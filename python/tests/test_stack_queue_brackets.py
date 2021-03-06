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

def test_opening_and_closing_mathces_but_order_is_not_balaned():
    actual = validate_brackets("([)]")
    expected = False
    assert actual == expected

# def test_empty_bracket():
#     empty_arg = validate_brackets("")
#     with pytest.raises(Empty) as exception_message:
#         empty_arg
#     assert str(exception_message.value) == "Empty string"

# def test_a_string_without_brackets():
#     empty_arg = validate_brackets("daniel")
#     with pytest.raises(Exception) as exception_message:
#         empty_arg.validate_brackets()
#     assert str(exception_message.value) == "Argument does not contain brackets"
