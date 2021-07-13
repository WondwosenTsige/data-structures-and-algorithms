from code_challenges.stacks_and_queue.queue.queue import Queue
import pytest
from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AniamlShelter

def test_can_enquee_animal():
    new_animal = AniamlShelter()
    new_animal.enqueue("dog")
    actual = new_animal.dogs.front.value
    expected = "dog"
    assert actual == expected

def test_enqueue_other_than_dig_or_cat_raise_exception():
    other_animal = AniamlShelter()
    with pytest.raises(Exception) as exception_message:
        other_animal.enqueue("rat")
    assert str(exception_message.value) == "only cats or dogs"


def test_can_dequeue_animal():
    new_animal = AniamlShelter()
    new_animal.enqueue("cat")
    actual = new_animal.dequeue("cat")
    expected = "cat"
    assert actual == expected

def test_dequeeing_an_unavailable_animal_will_raise_exception():
    empty_animal = Queue()
    with pytest.raises(Exception):
        empty_animal.dequeue()
