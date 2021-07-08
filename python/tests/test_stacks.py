import pytest

from code_challenges.stacks_and_queue.stacks import Stack

def test_Can_successfully_instantiate_an_empty_stack():
    new_stack = Stack()
    actual = new_stack.top
    expected = None
    assert actual == expected

def test_can_successfully_push_onto_a_stack():
    new_stack = Stack()
    new_stack.push("a")
    actual = new_stack.top.value
    expected = "a"
    assert actual == expected

def test_can_successfully_push_multiple_values_onto_a_stack(new_stack):
    actual = new_stack.top.value
    expected = "e"
    assert actual == expected

def test_can_successfully_pop_off_the_stack(new_stack):
    actual = new_stack.pop()
    expected = "e"
    assert actual == expected
    assert new_stack.top.value == "d"

def test_can_successfully_empty_a_stack_after_multiple_pops(new_stack):
    while not new_stack.isEmpty():
        new_stack.pop()
    assert new_stack.top == None

def test_can_successfully_peek_the_next_item_on_the_stack(new_stack):
    actual = new_stack.peek()
    expected = "e"
    assert actual == expected

def test_calling_pop_on_empty_stack_raises_exception():
    new_stack = Stack()
    with pytest.raises(Exception):
        new_stack.pop()

def test_calling_peek_on_empty_stack_raises_exception():
    new_stack = Stack()
    with pytest.raises(Exception):
        new_stack.peek()

"""
 Fixtures
"""

@pytest.fixture
def new_stack():
    new_stack = Stack()
    new_stack.push("a")
    new_stack.push("b")
    new_stack.push("c")
    new_stack.push("d")
    new_stack.push("e")
    return new_stack

# I need to read more on the following fixture
@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    new_stack = None
