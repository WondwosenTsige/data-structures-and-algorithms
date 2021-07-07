class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, node=None):
        self.front = node
        self.rear = node

    def enqueue(self, value):
        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear = node
            return self

        self.rear.next = node
        self.rear = node
        return self

    def dequeue(self):

        if self.front is None:
            raise Exception("Queue is empty")

        temp = self.front.value
        self.front = self.front.next
        return temp

    def peek(self):

        if self.front is None:
            raise Exception("Queue is empty")

        return self.front.value

    def isEmpty(self):

        return self.front == None


# if __name__ == "__main__":
#     pass
