from binarytree import BinaryTree


def test_BinaryTree():
    r = BinaryTree('a')
    assert r.get_root_val() == 'a'
    assert r.get_left_child() is None
    r.insert_left('b')
    assert str(r.get_left_child()) == 'BinaryTree object: val=b'
    assert r.get_left_child().get_root_val() == 'b'
    r.insert_right('c')
    assert str(r.get_right_child()) == 'BinaryTree object: val=c'
    assert r.get_right_child().get_root_val() == 'c'
    r.get_right_child().set_root_val('hello')
    assert r.get_right_child().get_root_val() == 'hello'
