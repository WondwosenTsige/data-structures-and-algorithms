import pytest
from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AniamlShelter

def test_can_enquee_animal():
    new_animal = AniamlShelter()
    new_animal.enqueue("dog")
    actual = new_animal.dogs.front.value
    expected = "dog"
    assert actual == expected


