class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        return self

    def pop(self):
        if self.top is None:
            raise Exception("Stack is Empty")
            # return None
        popped = self.top.value
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            raise Exception("Stack is Empty")
            # return None
        return self.top.value

    def isEmpty(self):
        return self.top == None


if __name__ == "__main__":
    pass
