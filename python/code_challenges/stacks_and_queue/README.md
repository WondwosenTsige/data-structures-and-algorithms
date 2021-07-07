## Challenge description

Stack

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

Create a Node class that has properties for the value stored in the Node, and a pointer to the next node

Create a Stack class that has a top property. It creates an empty Stack when instantiated.

This object should be aware of a default empty value assigned to top when the stack is created.

The class should contain the methods push, pop, peek, and isepmty

Queue

Create a Queue class that has a front property. It creates an empty Queue when instantiated.

This object should be aware of a default empty value assigned to front when the queue is created.

The class should contain the following methods enqueue, dequeue, peek, and isempty.


## Link to code

[Stack code](code_challenges/stacks_and_queue/stacks/stacks.py)
[Queue code](code_challenges/stacks_and_queue/queue/queue.py)
[Test stack](tests/test_stacks.py)
[Test Queue](tests/test_queue.py)

## Unit Tests Required

Can successfully push onto a stack

Can successfully push multiple values onto a stack

Can successfully pop off the stack

Can successfully empty a stack after multiple pops

Can successfully peek the next item on the stack

Can successfully instantiate an empty stack

Calling pop or peek on empty stack raises exception

Can successfully enqueue into a queue

Can successfully enqueue multiple values into a queue

Can successfully dequeue out of a queue the expected value

Can successfully peek into a queue, seeing the expected value

Can successfully empty a queue after multiple dequeues

Can successfully instantiate an empty queue

Calling dequeue or peek on empty queue raises exception

## approach and efficiency

Push
    Big O ----> Time:O(1)

Pop
    Big O ----> Time:O(1)

Enqueue
    Big O ----> Time:O(1)

Dequeue
    Big O ----> Time:O(1)

Peek
    Big O ----> Time:O(1)

isEmpty
    Big O ----> Time:O(1)

## Resources and Collaboration

This is done in collaboration with my class mates Daniel Dills, Davve Sok, and Micheal Ryan

We use the google to get the idea of raising exceptions.
