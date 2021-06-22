class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, node=None):
        # initialization here
        self.head = node


    def append(self, new_value):

        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last.next = new_node

    def insert_before(self, value, new_value):

        if self.head is None:
            print("ll is empty")
            return
        if self.head.value == new_value:
            new_node = Node(value)
            new_node.ref = self.head
            self.head = new_node
            return
        node = self.head
        while node.ref != None:
            if node.ref.value == new_value:
                break
            node = node.ref
        if node.ref is None:
            print("Node not found")
        else:
            new_node = node(value)
            new_node.ref = node.ref
            node.ref = new_node




    def insert_after(self, value, new_value):


        if value is None:
            print("value is not in linkedlist")
            return

        new_node = Node(new_value)
        new_node.next = value.next

        value.next = new_node



