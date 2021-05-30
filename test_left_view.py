import pytest
from bin_tree_view import *


def test_two_level_simple():
    t1_root = Node(1, Node(2), Node(3))
    assert LeftView(t1_root).left_view == [1, 2] + [-1] * 8

def test_null_tree():
    assert LeftView(None).left_view == [-1] * 10
