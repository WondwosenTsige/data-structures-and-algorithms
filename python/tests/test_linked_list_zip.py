from code_challenges.linked_list.linked_list import LinkedList


def test_one_of_the_linked_lists_is_empty():
    linkedlist1 = LinkedList()
    linkedlist1.append("a")
    actual = linkedlist1.head.value
    expected = "{'a'} ->  None"
    assert actual == expected


