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

    def insert(self, value):
        # method body here
        #create a new node
        node = Node(value)

        node.next = self.head
        self.head = node
        return self

    def includes(self, target):
        current = self.head

        while current != None:
            if current.value == target:
                return True
            current = current.next
        return False

    def __str__(self):
        string = ""
        #Making current to equal the first node
        current = self.head

        while current != None:
            string += f"{ {current.value} } -> "
            current = current.next
        string += f" None "
        return string

    def append(self, new_value):
        #Create a new node
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return self
        current = self.head
        while current.head != None:
            current = current.next
        current.next = new_node
        return self

    def insert_before(self, target, new_value):
        new_node = Node(new_value)

        if self.head is None:
            print("Empty linked list")

        if self.head.value == target:
            new_node.next = self.head
            self.head = new_node
            return self

        current = self.head
        while current != None:
            if current.next.value == target:
                new_node.next = new_node
                return self
            current = current.next
        print("Taregt not found in the linked list")


    def insert_after(self, target, new_value):
        new_node = Node(new_value)
        if self.head is None:
            print("Empty linked list")

        current = self.head
        while current != None:
            if current.value == target:
                new_node.next = new_node
                return self
            current = current.next
        print("Taregt not found in the linked list")
