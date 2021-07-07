import pytest

from stacks.stacks import Node, Stack
from stack_queue_pseudo.stack_queue_pseuodo import PseuedoQueue


def test_can_instantiate_a_new_PseuedoQueue_class():
    new_pseudo = PseuedoQueue()
    actual1 = new_pseudo.stack1.top
    actual2 = new_pseudo.stack2.top
    expected1 = None
    expected2 = None
    assert actual1 == expected1
    assert actual2 == expected2


def test_can_succefully_enqueue_one_value():
    new_pseudo = PseuedoQueue()
    new_pseudo.enqueue("a")
    actual = new_pseudo.stack1.top.value
    expected = "a"
    assert actual == expected


def test_can_succesfully_enqueue_multiple_values(new_pseudo):
    actual1 = new_pseudo.stack1.top.value
    expected1 = "d"
    actual2 = new_pseudo.stack1.top.next.value
    expected2 = "c"
    assert actual1 == expected1
    assert actual2 == expected2


def test_can_succesfully_dequeue_one_node(new_pseudo):
    actual = new_pseudo.dequeue()
    expected = "a"
    assert actual == expected


def test_can_succesfully_dequeue_until_empty(new_pseudo):
    while not new_pseudo.isEmpty():
        new_pseudo.dequeue()
    assert new_pseudo.stack1.isEmpty()


def test_dequeeing_an_empty_queue_will_raise_exception():
    empty_pseudo = PseuedoQueue()
    with pytest.raises(Exception):
        empty_pseudo.dequeue()


######################
# Fixtures
######################


@pytest.fixture
def new_pseudo():
    new_pseudo = PseuedoQueue()
    new_pseudo.enqueue("a")
    new_pseudo.enqueue("b")
    new_pseudo.enqueue("c")
    new_pseudo.enqueue("d")
    return new_pseudo


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    new_pseudo = None
