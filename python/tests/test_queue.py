import pytest

from code_challenges.stacks_and_queue.queue.queue import Queue

def test_Can_successfully_instantiate_an_empty_queue():
    new_queue = Queue()
    assert new_queue.front == None
    assert new_queue.rear == None

def test_Can_successfully_enqueue_one_value_into_a_queue():
    new_queue = Queue()
    new_queue.enqueue("a")
    assert new_queue.front.value == "a"
    assert new_queue.rear.value == "a"

def test_Can_successfully_enqueue_multiple_values_into_a_queue(new_queue):
    assert new_queue.front.value == "a"
    assert new_queue.front.next.value == "b"
    assert new_queue.rear.value == "e"

def test_Can_successfully_dequeue_off_the_queue(new_queue):
    actual = new_queue.dequeue()
    expected = "a"
    assert actual == expected
    assert new_queue.front.value == "b"

def test_Can_successfully_empty_a_queue_after_multiple_dequeues(new_queue):
    while not new_queue.isEmpty():
        new_queue.dequeue()
    assert new_queue.front == None

def test_Calling_dequeue_on_empty_queue_raises_exception():
    new_queue = Queue()
    with pytest.raises(Exception):
        new_queue.dequeue()

def test_Calling_peek_on_empty_queue_raises_exception():
    new_queue = Queue()
    with pytest.raises(Exception):
        new_queue.peek()

# Understand what fixture is doing here for the first time
@pytest.fixture
def new_queue():
    new_queue = Queue()
    new_queue.enqueue("a")
    new_queue.enqueue("b")
    new_queue.enqueue("c")
    new_queue.enqueue("d")
    new_queue.enqueue("e")
    return new_queue

# Need to read more here
@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    new_queue = None
