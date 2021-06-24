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

## Collaboration

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
