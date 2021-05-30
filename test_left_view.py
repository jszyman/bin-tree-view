import pytest
from bin_tree_view import Node, LeftView


def test_null_tree():
    """
    tested tree: None
    """
    assert LeftView(None).left_view == [-1] * 10


def test_one_level():
    """
    tested tree: 1
    """
    assert LeftView(Node(1)).left_view == [1] + [-1] * 9


def test_two_level_simple():
    """
    tested tree:
      1
     / \
    2   3
    """
    t1_root = Node(1, Node(2), Node(3))
    assert LeftView(t1_root).left_view == [1, 2] + [-1] * 8

def test_two_level_left_branch_longer():
    """
    tested tree:
      1
     /
    2
    """
    t1_root = Node(1, left_node=Node(2))
    assert LeftView(t1_root).left_view == [1, 2] + [-1] * 8


def test_three_level_with_one_leaf_missing():
    """
    tested tree:
        1
     /    \
    2      3
   | |    /
  4  5   6
    """
    t1_root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))
    assert LeftView(t1_root).left_view == [1, 2, 4] + [-1] * 7


def test_four_level_with_more_leafs_missing():
    """
    tested tree:
        1
     |     \
    2       3
     |     /
      5   6
         |
        7
    """
    t1_root = Node(1, left_node=Node(2, right_node=Node(5)), right_node=Node(3, left_node=Node(6, left_node=Node(7))))
    assert LeftView(t1_root).left_view == [1, 2, 5, 7] + [-1] * 6


def test_four_level_only_one_leaf():
    """
    tested tree:
        1
         \
          3
         /
        6
         \
         7
    """
    t1_root = Node(1, right_node=Node(3, left_node=Node(6, right_node=Node(7))))
    assert LeftView(t1_root).left_view == [1, 3, 6, 7] + [-1] * 6


def test_four_level_only_one_leaf_except_root():
    """
    tested tree:
        1
      /   \
     2     3
          /
         6
          \
           7
    """
    t1_root = Node(1, left_node=Node(2), right_node=Node(3, left_node=Node(6, right_node=Node(7))))
    assert LeftView(t1_root).left_view == [1, 2, 6, 7] + [-1] * 6
