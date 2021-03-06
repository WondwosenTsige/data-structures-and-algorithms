# Singly Linked List: lab-05
<!-- Short summary or background information -->


## Challenge

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.

Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

Define a method called __str__ which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency

I used Single-responsibility principle: by defining one function for every other test case so that it would only solve one problem and I can

Successfully instantiate an empty linked list

Able to properly insert into the linked list

Check if the head property will properly point to the first node in the linked list

Poperly insert multiple nodes into the linked list

Able to return True when finding a value within the linked list that exists

Able to return False when searching for a value in the linked list that does not exist

Able to return a collection of all the values that exist in the linked list

### Collaboration

For this code challenge, I collaborated with Davee Sok, Daniel Dills and Michael Ryan

## Linked list insertions: lab-06

### Challenge description

Extend the LinkedList class to allow various insertion methods:

- .append(value) which adds a new node with the given value to the end of the list.

- .nsertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node

- .nsertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

### Unit Tests Required

1. Can successfully add a node to the end of the linked list

2. Can successfully add multiple nodes to the end of a linked list

3. Can successfully insert a node before a node located i the middle of a linked list

4. Can successfully insert a node before the first node of a linked list

5. Can successfully insert after a node in the middle of the linked list

6. Can successfully insert a node after the last node of the linked list

### Whiteboard image

[Whiteboard image: Linked list insertion](/home/wonde/codefellows/code-401/data-structures-and-algorithms/python/code_challenges/images/ll-insertion.jpg)

### approach and efficiency

### Resources and Collaboration

This is a paired assignment with Gleen Clark

We use the following websites as reference and sample codes

    https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

    https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/

    https://stackoverflow.com/questions/61839128/edge-cases-in-creating-a-custom-linked-list

    https://www.geeksforgeeks.org/insert-a-node-in-linked-list-before-a-given-node/


## Linked list kth: lab-07

### Challenge description

Write the following method for the Linked List class:

- kth from end

- argument: a number, k, as a parameter.

- Return the node’s value that is k places from the tail of the linked list.

- You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

### Unit Tests Required

1. Where k is greater than the length of the linked list

2. Where k and the length of the list are the same

3. Where k is not a positive integer

4. Where the linked list is of a size 1

5. “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

### whiteboard image

[Whiteboard image: linked list kth](/home/wonde/codefellows/code-401/data-structures-and-algorithms/python/code_challenges/images/linked-list-kth.jpg)

### Approach and efficieny


### Collaboration

This assignment is a group work in collaboration with Garfield Grant, Prabin Singh, and Gleen Clark.
