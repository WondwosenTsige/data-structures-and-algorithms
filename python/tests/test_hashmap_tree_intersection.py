import pytest
from code_challenges.hashmap_tree_intersection.hashmap_tree_intersection import hash_intersection
from code_challenges.trees.trees import BinaryTree, Node


def test_proof_of_life():
    assert hash_intersection

def test_node_n_tree():
    tree = BinaryTree()
    node = Node(0)
    assert tree
    assert node

def test_tree1(binary_tree,binary_tree2 ):
    actual = hash_intersection(binary_tree, binary_tree2)
    expected =  [1, 15]
    assert actual == expected

def test_no_duplicates(binary_tree, binary_tree3):
    actual = hash_intersection(binary_tree,binary_tree3)
    expected = []
    assert actual == expected





@pytest.fixture
def binary_tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(5)
    tree.root.right = Node(10)
    tree.root.left.right = Node(25)
    tree.root.left.right.left = Node(13)
    tree.root.left.right.right = Node(15)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree

@pytest.fixture
def binary_tree2():
    tree2= BinaryTree()
    tree2.root = Node(1)
    tree2.root.left = Node(15)
    tree2.root.right = Node(12)
    tree2.root.left.right = Node(23)
    tree2.root.left.right.left = Node(3)
    tree2.root.left.right.right = Node(55)
    tree2.root.right.right = Node(19)
    tree2.root.right.right.left = Node(34)

    return tree2

@pytest.fixture
def binary_tree3():
    tree3 = BinaryTree()
    tree3.root = Node(2)
    tree3.root.left = Node(18)
    tree3.root.right = Node(6)
    tree3.root.left.right = Node(8)
    tree3.root.left.right.left = Node(20)
    tree3.root.left.right.right = Node(12)
    tree3.root.right.right = Node(14)
    tree3.root.right.right.left = Node(16)
    return tree3
