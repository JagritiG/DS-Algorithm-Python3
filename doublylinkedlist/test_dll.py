from dll import DLLNode, DLL


class TestClassDll():

        def test_getData(self):
                node = DLLNode('Python')
                assert node.getData() == 'Python'

        def test_setData(self):
                node = DLLNode('Python')
                node.setData(8)
                assert node.getData() == 8

        def test_setNext(self):
                node = DLLNode('Python')
                node2 = DLLNode('java')
                node.setNext(node2)
                result = str(node.getNext())
                expected = 'DLLNode object: data=java'
                assert result == expected

        def test_setPrevious(self):
                node = DLLNode(3)
                node2 = DLLNode(4)
                node.setPrevious(node2)
                result = str(node.getPrevious())
                expected = 'DLLNode object: data=4'
                assert result == expected

        def test_isEmptyDLL(self):
                dll = DLL()
                assert dll.isEmpty() == True
                node = DLLNode(1)
                dll.head = node
                assert dll.isEmpty() == False

        def test_addNode(self):
                dll = DLL()
                dll.head
                dll.addNode(1)
                assert str(dll.head) == 'DLLNode object: data=1'
                assert dll.head.previous == None
                assert dll.head.next == None
                dll.addNode(2)
                assert str(dll.head) == 'DLLNode object: data=2'
                assert dll.head.previous == None
                assert str(dll.head.next) == 'DLLNode object: data=1'
                assert dll.size() == 2
                assert dll.head.next.next == None

        def test_size(self):
                dll = DLL()
                size = dll.size()
                # Test an empty Linked List
                assert size == 0
                # Test Linked List with some nodes
                dll.addNode(1)
                dll.addNode(2)
                dll.addNode(3)
                size = dll.size()
                assert size == 3

        def test_search(self):
                dll = DLL()
                # Test an empty Linked List
                assert dll.search(5) == 'Linked List is empty.'
                # Test Linked List with some nodes
                dll.addNode(1)
                dll.addNode(2)
                dll.addNode(3)
                assert dll.search('python') == False
                assert dll.search(3) == True

        def test_remove(self):
                dll = DLL()
                # Test an empty Linked List
                assert str(dll.remove(5)) == 'Linked List is empty. No Nodes to remove.'
                # Test Linked List with some nodes
                dll.addNode(1)
                dll.addNode(2)
                assert str(dll.remove(24)) == 'A Node with given data is not present.'
                assert dll.search(2) == True
                dll.remove(2)
                assert dll.search(2) == False
                dll.addNode(3)
                assert dll.size() == 2
                assert str(dll.head) == 'DLLNode object: data=3'
                dll.remove(3)
                assert str(dll.head) == 'DLLNode object: data=1'


