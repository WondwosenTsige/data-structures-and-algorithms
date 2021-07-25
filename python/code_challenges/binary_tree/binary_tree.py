class Node:
    """
    Docstring
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Docstring
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

    def add():
        pass

    def contains():
        pass
