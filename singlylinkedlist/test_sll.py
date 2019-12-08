from singlylinkedlist.sll import SLLNode, SLL


class TestClassSll:

        def test_get_data(self):
                node = SLLNode('apple')
                assert node.get_data() == 'apple'

        def test_set_data(self):
                node = SLLNode('apple')
                node.set_data(8)
                assert node.get_data() == 8

        def test_set_next(self):
                node = SLLNode('apple')
                node2 = SLLNode('orange')
                node.set_next(node2)
                result = str(node.get_next())
                expected = 'orange'
                assert result == expected

        def test_is_emptySLL(self):
                sll = SLL()
                assert sll.is_empty() == True
                node = SLLNode(1)
                sll.head = node
                assert sll.is_empty() == False

        def test_add_node_at_head(self):
                sll = SLL()
                sll.head()
                sll.add_node_at_head('cpp')
                result = str(sll.head)
                expected = 'cpp'
                assert result == expected

        def test_size(self):
                sll = SLL()
                size = sll.size()
                # Test an empty Linked List
                assert size == 0
                # Test Linked List with some nodes
                sll.add_node_at_head(1)
                sll.add_node_at_head(2)
                sll.add_node_at_head(3)
                sll.add_node_at_head(4)
                size = sll.size()
                assert size == 4

        def test_search(self):
                sll = SLL()
                # Test an empty Linked List
                assert sll.search(5) == 'Linked List is empty.'
                # Test Linked List with some nodes
                sll.add_node_at_head(1)
                sll.add_node_at_head(2)
                sll.add_node_at_head(3)
                assert sll.search('python') == False
                assert sll.search(3) == True

        def test_remove(self):
                sll = SLL()
                # Test an empty Linked List
                assert str(sll.remove(5)) == 'Linked List is empty. No Nodes to remove.'
                # Test Linked List with some nodes
                sll.add_node_at_head(1)
                sll.add_node_at_head(2)
                sll.add_node_at_head(3)
                assert str(sll.remove(24)) == 'A Node with given data is not present.'
                assert sll.search(2) == True
                sll.remove(2)
                assert sll.search(2) == False




