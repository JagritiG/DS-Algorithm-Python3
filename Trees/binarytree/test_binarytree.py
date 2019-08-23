from binarytree import BinaryTree


def test_binaryTree():
    r = BinaryTree(3)
    assert r.root == 3
    assert r.getRoot() == 3
    assert r.getLeftChild() is None
    r.insertLeftChild(4)
    assert str(r.getLeftChild()) == 'BinaryTree object: node=4'
    assert r.getLeftChild().getRoot() == 4
    r.insertRightChild(5)
    assert str(r.getRightChild()) == 'BinaryTree object: node=5'
    assert r.getRightChild().getRoot() == 5
    r.getRightChild().setRoot(6)
    assert r.getRightChild().getRoot() == 6




