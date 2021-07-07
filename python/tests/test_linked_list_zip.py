from code_challenges.linked_list_zip.linked_list_zip import LinkedList

def test_one_of_the_linked_lists_is_empty():
    linkedlist1 = LinkedList()
    assert linkedlist1.head == None

# def test_zip_list():
#     linkedlist1 = LinkedList(Node('1', Node('3', Node('5'))))
#     linkedlist2 = LinkedList(Node('2', Node('4', Node('6'))))
#     zip_list(linkedlist1, linkedlist2)
#     actual = linkedlist2.__str__()
#     expected = "{'1'} -> {'2'} -> {'3'} -> {'4'} -> {'5'} -> {'6'} -> NULL"
#     assert actual == expected

# def test_zip_list_diff_size():
#     linkedlist1 = LinkedList(Node('1', Node('3', Node('5'))))
#     linkedlist2 = LinkedList(Node('2', Node('4')))
#     zip_list(linkedlist1, linkedlist2)
#     actual = linkedlist2.__str__()
#     expected = "{'1'} -> {'2'} -> {'3'} -> {'4'} -> {'5'} -> NULL"
#     assert actual == expected
