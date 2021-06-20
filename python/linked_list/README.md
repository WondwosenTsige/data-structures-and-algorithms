# Singly Linked List
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
