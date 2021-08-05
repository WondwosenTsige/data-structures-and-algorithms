import pytest
from code_challenges.fizz_buzz_tree.fizz_buzz_tree import K_node, K_Tree, fizz_buzz_helper, fizz_buzz_tree
def test_can_instantiate_K_node():
    k_node = K_node(3)
    assert k_node.value == 3
    assert k_node.children == []


def test_can_instantiate_empty_K_tree():
    new_k_tree = K_Tree()
    assert new_k_tree.root == None


def test_can_instantiate_K_tree_with_one_node():
    knode = K_node(10)
    new_k_tree = K_Tree(knode)
    assert new_k_tree.root.value == 10
    assert new_k_tree.root.children == []


def test_k_tree_breadth_first_method_returns_correct_values(new_tree):
    actual = new_tree.breadth_first()
    expected = [1, 2, 3, 4, 5, 11, 6, 7, 10, 8, 9, 12, 13, 14]
    assert actual == expected


def test_fizz_buzz_helper_returns_fizz(new_tree):
    assert fizz_buzz_helper(3) == "Fizz"


def test_fizz_buzz_helper_returns_buzz():
    assert fizz_buzz_helper(10) == "Buzz"


def test_fizz_buzz_helper_returns_fizzbuzz():
    assert fizz_buzz_helper(15) == "FizzBuzz"


def test_fizz_buzz_helper_returns_string():
    assert fizz_buzz_helper(7) == "7"


def test_fizz_buzz_tree_raises_error_on_empty_tree():
    empty_tree = K_Tree()
    with pytest.raises(Exception):
        fizz_buzz_tree(empty_tree)


def test_fizz_buzz_tree_return_corrrect_values(new_tree):
    fizz_buzz_tree(new_tree)
    actual = new_tree.breadth_first()
    expected = ["1", "2", "Fizz", "4", "Buzz", "11", "Fizz", "7", "Buzz", "8", "Fizz", "Fizz", "13", "14"]
    assert actual == expected


######################
# Fixtures
######################


@pytest.fixture
def new_tree():
    node8 = K_node(8)
    node9 = K_node(9)
    node12 = K_node(12)
    node13 = K_node(13)
    node14 = K_node(14)
    node5 = K_node(5)
    node11 = K_node(11)
    node7 = K_node(7)
    node10 = K_node(10)
    node4 = K_node(4, [node8, node9])
    node6 = K_node(6, [node12, node13, node14])
    node2 = K_node(2, [node4, node5, node11])
    node3 = K_node(3, [node6, node7, node10])
    node1 = K_node(1, [node2, node3])
    new_tree = K_Tree(node1)
    return new_tree


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    new_tree = None
