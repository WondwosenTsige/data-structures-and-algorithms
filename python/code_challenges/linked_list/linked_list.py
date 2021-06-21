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
        current = self.head

        while current != None:
            string += f"{ {current.value} } -> "
            current = current.next
        string += f" None "
        return string



# if __name__ == "__main__":
#     linkedlist1 = LinkedList()
#     linkedlist1.insert("a").insert("b").insert("c").insert("d")
#     result = str(linkedlist1)
#     print(result)
