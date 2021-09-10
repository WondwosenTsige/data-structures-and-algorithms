# Hash Tables

Specifications
Read all of these instructions carefully.
Name things exactly as described.
Do all your work in a your data-structures-and-algorithms public repository.
Create a new branch in your repo named as noted below.
Follow the language-specific instructions for the challenge type listed below.
Update the “Table of Contents” - in the README at the root of the repository - with a link to this challenge’s README file.

## Challenge Setup & Execution

Branch Name: hashtable

## Challenge Type: New Implementation

## Features

Implement a Hashtable Class with the following methods:

add
    Arguments: key, value
    Returns: nothing
    This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
get
    Arguments: key
    Returns: Value associated with that key in the table
contains
    Arguments: key
    Returns: Boolean, indicating if the key exists in the table already.

hash
    Arguments: key
    Returns: Index in the collection for that key

## Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

    Adding a key/value to your hashtable results in the value being in the data structure
    Retrieving based on a key returns the value stored
    Successfully returns null for a key that does not exist in the hashtable
    Successfully handle a collision within the hashtable
    Successfully retrieve a value from a bucket within the hashtable that has a collision
    Successfully hash a key to an in-range value
    Ensure your tests are passing before you submit your solution.

## Collaboration and reference

I used the class repo as a reference and collaborated with Daniel Dills, Davee Sok, and Prabin Singh
