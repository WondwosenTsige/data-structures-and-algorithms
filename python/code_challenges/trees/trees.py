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

    def pre_order(self):
        # root >> left >> right

        if self.root is None:
            return "tree empty"

        collection = []
        def traverse(root):

            if root != None:
                collection.append(root.value)
                traverse(root.left)
                traverse(root.right)
        traverse(self.root)
        return collection


    def in_order(self):
        # left >> root >> right
        collection = []
        def traverse(root):

            if root != None:
                traverse(root.left)
                collection.append(root.value)
                traverse(root.right)
        traverse(self.root)
        return collection

    def post_order(self):
        # left >> right >> root
        collection = []
        def traverse(root):

            if root != None:
                traverse(root.left)
                traverse(root.right)
                collection.append(root.value)
        traverse(self.root)
        return collection





class BinarySearchTree(BinaryTree):

    """
This class should be a sub-class of the Binary Tree Class, with the following additional methods:

"""
    def __init__(self):
        self.root = None

    def add(self, value):

        node = Node(value)

        if self.root == None:
            self.root = Node(value)
            return self

        current = self.root

        while current:
            if value == current.value:
                raise Exception("Value already exist")

            if value > current.value:
                if current.right is None:
                    current.right = node
                    return self
                current = current.right

            else:
                if current.left is None:
                    current.left = node
                    return self
                current = current.left


    def contains(self, target):

        if self.root is None:
            return None
        current = self.root

        while current:
            if current.value == target:
                return True
            if target > current.value:
                current = current.right
            else:
                current = current.left
        return False


