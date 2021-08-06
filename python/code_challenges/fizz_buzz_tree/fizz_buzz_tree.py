from code_challenges.stacks_and_queue.queue.queue import Queue
class K_node:

    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children


class K_Tree:
    def __init__(self, node=None):
        self.root = node

    def breadth_first(self):
        queue = Queue()
        queue.enqueue(self.root)
        result = []

        while not queue.isEmpty():
            front = queue.dequeue()
            for node in front.children:
                queue.enqueue(node)
            result.append(front.value)
        return result


def fizz_buzz_helper(num):

    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def fizz_buzz_tree(tree):

    if tree.root is None:
        raise Exception("Tree is empty")

    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.isEmpty():
        front = queue.dequeue()
        front.value = fizz_buzz_helper(front.value)
        for node in front.children:
            queue.enqueue(node)

    return tree


if __name__ == "__main__":
    node8 = K_node(8)
    node9 = K_node(9)
    node12 = K_node(12)
    node13 = K_node(13)
    node14 = K_node(14)
    node5 = K_node(5)
    node11 = K_node(11)
    node7 = K_node(7)
    node10 = K_node(10)
    node4 = K_node(4, [node8, node9])
    node6 = K_node(6, [node12, node13, node14])
    node2 = K_node(2, [node4, node5, node11])
    node3 = K_node(3, [node6, node7, node10])
    node1 = K_node(1, [node2, node3])
    new_tree = K_Tree(node1)
    print(new_tree)
