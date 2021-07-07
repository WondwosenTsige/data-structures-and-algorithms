from stacks_and_queue.stacks.stacks import Node, Stack


class PseuedoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):

        if self.stack1.isEmpty():
            raise Exception("PseudoQueue is Empty")

        while not self.stack1.isEmpty():
            popped = self.stack1.pop()
            self.stack2.push(popped)

        dequed = self.stack2.pop()

        while not self.stack2.isEmpty():
            popped = self.stack2.pop()
            self.stack1.push(popped)

        return dequed

    def isEmpty(self):
        return self.stack1.isEmpty()


if __name__ == "__main__":
    pass
