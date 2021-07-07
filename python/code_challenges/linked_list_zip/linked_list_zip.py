class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, node = None):
        self.head = node


    def __str__(self):
            string = ""
            #Making current to equal the first node
            current = self.head
            while current:
                string += current.value
                current  = current.next
            return string

def zip_list(linkedlist1, linkedlist2):

        linkedlist1_curr = linkedlist1.head
        linkedlist2_curr = linkedlist2.head

        while linkedlist1_curr != None and linkedlist2_curr != None:

            #Save next pointers
            linkedlist1_next = linkedlist1_curr.next
            linkedlist2_next = linkedlist2_curr.next
            linkedlist2_curr.next = linkedlist1_next # change next pointer of q_curr
            linkedlist1_curr.next = linkedlist2_curr # change next pointer of p_curr
            linkedlist1_curr = linkedlist1_next
            linkedlist2_curr = linkedlist2_next

        linkedlist2.head = linkedlist2_curr
