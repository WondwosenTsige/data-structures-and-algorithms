from code_challenges.stacks_and_queue.queue import Queue


def graph_breadth_first(vertex):
    nodes = []
    breadth = Queue()
    visited = set()

    breadth.enqueue(vertex)
    visited.add(vertex)

    while not breadth.isEmpty():
        front = breadth.dequeue()
        nodes.append(front)

        for neighbor in front.neighbor:
            if neighbor.vertex not in visited:
                visited.append(neighbor)
                breadth.enqueue(neighbor)

    return nodes
