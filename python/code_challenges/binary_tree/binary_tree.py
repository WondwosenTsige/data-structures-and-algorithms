class Node:
    """
    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Create a Binary Tree class
        Define a method for each of the depth first traversals:
            pre order
            in order
            post order which returns an array of the values, ordered appropriately.
    """
    def __init__(self):
        self.root = None

    def pre_order():
        # root >> left >> right

        collection = []
        def traverse(root):

            if root != None:
                collection.append(root.value)
                traverse(root.left)
                traverse(root.right)
            return collection


    def in_order():
        # left >> root >> right
        collection = []
        def traverse(root):

            if root != None:
                traverse(root.left)
                collection.append(root.value)
                traverse(root.right)
            return collection

    def post_order():
        # left >> right >> root
        collection = []
        def traverse(root):

            if root != None:
                traverse(root.left)
                traverse(root.right)
                collection.append(root.value)
            return collection





class BinarySearchTree(BinaryTree):

    """
This class should be a sub-class of the Binary Tree Class, with the following additional methods:

"""
    def __init__(self):
        self.root = None

    def add(self, value):

        if self.root == None:
            self.root = Node(value)
            return


    def contains():
        pass
