from singlylinkedlist.singly_linkedlist import SllNode, Sll


class TestClassSll:

        def test_get_data(self):
                node = SllNode('apple')
                assert node.get_data() == 'apple'

        def test_set_data(self):
                node = SllNode('apple')
                node.set_data(8)
                assert node.get_data() == 8

        def test_set_next(self):
                node = SllNode('apple')
                node2 = SllNode('orange')
                node.set_next(node2)
                result = str(node.get_next())
                expected = 'orange'
                assert result == expected

        def test_is_empty(self):
                sll = Sll()
                assert sll.is_empty() is True
                node = SllNode(1)
                sll.head = node
                assert sll.is_empty() is False

        def test_add_at_head(self):
                sll = Sll()
                sll.add_at_head('cpp')
                result = str(sll.head)
                expected = 'cpp'
                assert result == expected

        def test_add_at_tail(self):
            pass

        def test_insert_at_nth_pos(self):
            pass

        def test_delete_nth_node(self):
            pass

        def test_list_size(self):
                sll = Sll()
                size = sll.list_size()
                # Test an empty Linked List
                assert size == 0
                # Test Linked List with some nodes
                sll.add_at_head(1)
                sll.add_at_head(2)
                sll.add_at_head(3)
                sll.add_at_head(4)
                size = sll.list_size()
                assert size == 4

        def test_search(self):
                sll = Sll()
                # Test an empty Linked List
                assert sll.search(5) == 'Linked list is empty'
                # Test Linked List with some nodes
                sll.add_at_head(1)
                sll.add_at_head(2)
                sll.add_at_head(3)
                assert sll.search('python') is False
                assert sll.search(3) is True

        def test_remove(self):
                sll = Sll()
                # Test an empty Linked List
                assert sll.remove(5) == "Linked list is empty"
                # Test Linked List with some nodes
                sll.add_at_head(1)
                sll.add_at_head(2)
                sll.add_at_head(3)
                assert str(sll.remove(24)) == 'A Node with given data is not present.'
                assert sll.search(2) is True
                sll.remove(2)
                assert sll.search(2) is False

        def test_reverse_iter(self):
                sll = Sll()
                sll.add_at_head(1)
                sll.add_at_head(2)
                sll.add_at_head(3)
                result = str(sll.head)
                assert result == str(3)
                sll.reverse_iter()
                assert str(sll.head) == str(1)

        def test_print_list(self):
            pass


