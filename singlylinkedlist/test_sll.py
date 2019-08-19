from sll import SLLNode, SLL


class TestClassSll:

        def test_getData(self):
                node = SLLNode('apple')
                assert node.getData() == 'apple'

        def test_setData(self):
                node = SLLNode('apple')
                node.setData(8)
                assert node.getData() == 8

        def test_setNext(self):
                node = SLLNode('apple')
                node2 = SLLNode('orange')
                node.setNext(node2)
                result = str(node.getNext())
                expected = 'SLLNode object: data=orange'
                assert result == expected

        def test_isEmptySLL(self):
                sll = SLL()
                assert sll.isEmpty() == True
                node = SLLNode(1)
                sll.head = node
                assert sll.isEmpty() == False

        def test_addNode(self):
                sll = SLL()
                sll.head
                sll.addNode('cpp')
                result = str(sll.head)
                expected = 'SLLNode object: data=cpp'
                assert result == expected

        def test_size(self):
                sll = SLL()
                size = sll.size()
                # Test an empty Linked List
                assert size == 0
                # Test Linked List with some nodes
                sll.addNode(1)
                sll.addNode(2)
                sll.addNode(3)
                sll.addNode(4)
                size = sll.size()
                assert size == 4

        def test_search(self):
                sll = SLL()
                # Test an empty Linked List
                assert sll.search(5) == 'Linked List is empty.'
                # Test Linked List with some nodes
                sll.addNode(1)
                sll.addNode(2)
                sll.addNode(3)
                assert sll.search('python') == False
                assert sll.search(3) == True

        def test_remove(self):
                sll = SLL()
                # Test an empty Linked List
                assert str(sll.remove(5)) == 'Linked List is empty. No Nodes to remove.'
                # Test Linked List with some nodes
                sll.addNode(1)
                sll.addNode(2)
                sll.addNode(3)
                assert str(sll.remove(24)) == 'A Node with given data is not present.'
                assert sll.search(2) == True
                sll.remove(2)
                assert sll.search(2) == False




