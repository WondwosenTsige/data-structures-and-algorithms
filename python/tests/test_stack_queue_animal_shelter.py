import pytest
from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import Node, AniamlShelter

def test_can_enquee_animal():
    new_animal = AniamlShelter()
    new_animal.enqueue("dog")
    new_animal.enqueue("cat")
    """enqueing dog first cat second and then expecting to see
    if i enqued both values successfuly so that there is a first
    value and the next of it is the second value enqued cat"""
    actual = new_animal.first.next.value
    expected = "cat"
    assert actual == expected
