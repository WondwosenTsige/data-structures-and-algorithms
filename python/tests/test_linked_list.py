from code_challenges.linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList

def test_node_class_can_instanciate():
    #Creating a new node instance
    node1 = Node("mango")
    actual = node1.value
    expected = "mango"
    assert actual == expected
    assert node1.next == None

def test_can_instanciate_empty_list():
    linkedlist1 = LinkedList()
    actual = linkedlist1.head
    expected = None
    assert actual == expected

def test_can_insert_into_linkedt_list():
    linkedlist1 = LinkedList()
    linkedlist1.insert("a")
    linkedlist1.insert("b")
    actual = linkedlist1.head.value
    expected = "b"
    assert actual == expected

def test_head_point_to_first_node():
    node1 = Node("a")
    linkedlist1 = LinkedList(node1)
    actual = linkedlist1.head.value
    expected = "a"
    assert actual == expected

def test_can_insert_multiple_nodes_into_linked_list():
    linkedlist1 = LinkedList()
    linkedlist1.insert("a").insert("b").insert("c")
    actual = linkedlist1.head.value
    expected = "c"
    assert actual == expected

def test_will_return_True_when_value_found_in_linked_list():
    linklist1 = LinkedList()
    linklist1.insert("a").insert("b").insert("c").insert("d")
    actual = linklist1.includes("c")
    expected = True
    assert actual == expected


def test_will_return_False_when_value_not_found_in_linked_list():
    linklist1 = LinkedList()
    linklist1.insert("a").insert("b").insert("c").insert("d")
    actual = linklist1.includes("e")
    expected = False
    assert actual == expected

def test_can_return_all_values_existed_in_linked_list():
    linklist1 = LinkedList()
    linklist1.insert("a").insert("b").insert("c").insert("d")
    actual = str(linklist1)
    expected = "{'d'} -> {'c'} -> {'b'} -> {'a'} ->  None "
    assert actual == expected

def test_append():
    new_linkedlist = LinkedList()
    new_linkedlist.append("j")
    new_linkedlist.append("k")
    assert new_linkedlist.head.value == "j"

def test_insert_before_a_target_node():
    new_linkedlist = LinkedList()
    new_linkedlist.insert("w")
    new_linkedlist.append("x")
    new_linkedlist.insert_before("x","z")
    assert new_linkedlist.head.next.value == "z"

def test_insert_after_a_target_node():
    new_linkedlist = LinkedList()
    new_linkedlist.append("x")
    new_linkedlist.insert("z")
    new_linkedlist.insert_after("x", "z")
    assert new_linkedlist.head.next.next.value == "z"

def test_kth_value_is_negative():
    new_linkedlist = LinkedList()
    actual = new_linkedlist.kth_from_end(-1)
    expected = "Input is negative number"
    assert actual == expected

def test_kth_value_is_greater_than_the_linked_list():
    new_linkedlist = LinkedList()
    actual = new_linkedlist.kth_from_end(7)
    expected = "kth value is greater than the lenght of the linked list"
    assert actual == expected

def test_linkedlist_is_size_of_one():
    new_linkedlist = LinkedList()
    actual = new_linkedlist.kth_from_end(0)
    expected = "The linked list only has one node"
    assert actual == expected


# def test_linked_list_has_same_lenght_with_k():
#     new_linkedlist = LinkedList()
#     actual = new_linkedlist.kth_from_end(4)
#     expected = "K & the list are of the same Length"
#     assert actual == expected
