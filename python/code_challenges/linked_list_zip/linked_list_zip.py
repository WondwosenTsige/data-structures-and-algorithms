class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, node = None):
        self.head = node


def push(self, value):
        # method body here
        #create a new node
        node = Node(value)

        node.next = self.head
        self.head = node
        return self

def zip_lists(self, linkedlist2):
    linkedlist1_current = self.head
    linkedlist2_current = linkedlist2.head

    while linkedlist1_current != None and linkedlist2_current is not None:

        #Setting next pointers
        linkedlist1_next = linkedlist1_current.next
        linkedlist2_next = linkedlist2_current.next

        #Change next pointer of linkelist2 current
        #Change next pointer of linkelist1 current
        linkedlist2_current.next = linkedlist1_next
        linkedlist1_current.next = linkedlist2_next

        #Update current pointers for next iteration
        linkedlist1_current = linkedlist1_next
        linkedlist2_current = linkedlist2_next

    linkedlist2.head = linkedlist2_current



