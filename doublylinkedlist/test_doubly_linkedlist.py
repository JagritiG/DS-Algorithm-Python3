# Test bench for doubly linked list
from doublylinkedlist.doubly_linkedlist import DllNode, Dll


class TestDllNode:

    def test_get_data(self):
        node = DllNode(1)
        assert node.get_data() == 1

    def test_set_data(self):
        node = DllNode(1)
        node.set_data(2)
        assert node.get_data() == 2

    def test_set_next(self):
        node = DllNode(1)
        node2 = DllNode(2)
        node.set_next(node2)
        assert str(node.get_next()) == str(2)

    def test_set_previous(self):
        node = DllNode(1)
        node2 = DllNode(2)
        node.set_previous(node2)
        assert str(node.get_previous()) == str(2)

    def test_is_empty(self):
        dll = Dll()
        assert dll.is_empty() is True
        node = DllNode(1)
        dll.head = node
        assert dll.is_empty() is False

    def test_size(self):
        dll = Dll()
        size = dll.size_dll()
        # Test an empty Linked List
        assert size == 0
        # Test Linked List with some nodes
        dll.add_at_head(1)
        dll.add_at_head(2)
        dll.add_at_head(3)
        dll.add_at_head(4)
        size = dll.size_dll()
        assert size == 4

    def test_add_at_head(self):
        dll = Dll()
        dll.add_at_head("apple")
        dll.add_at_head("orange")
        assert str(dll.head) == "orange"

    def test_add_at_tail(self):
        dll = Dll()
        dll.add_at_head("apple")
        dll.add_at_head("orange")
        dll.add_at_tail("mango")
        assert str(dll.head) == "orange"
        assert dll.size_dll() == 3

    def test_add_at_nth_position(self):
        dll = Dll()
        dll.add_at_head(1)
        dll.add_at_head(2)
        dll.add_at_head(3)
        dll.add_at_head(4)
        dll.add_at_nth_position(5, 0)
        size = dll.size_dll()
        assert size == 5

    def test_delete_nth_node(self):
        pass

    def test_search(self):
        pass

    def test_remove(self):
        pass

    def test_print_dll(self):
        pass
