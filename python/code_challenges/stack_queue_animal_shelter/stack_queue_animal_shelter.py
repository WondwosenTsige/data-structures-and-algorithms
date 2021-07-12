class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class AniamlShelter():
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, animal):
        node = Node(animal)

        if self.first is None:
            self.first = node
            self.last = node
            return self

        #this is equivalent to else statement
        self.last.next = node
        self.last = node
        return self

    def dequeue(self, pref):
        node = Node(pref)

        if self.first is None:
            raise Exception("Queue is empty")

        elif pref == "dog" or pref == "cat":
            node = self.first
            self.first = self.first.next
            return node.value
        else:
            return None




