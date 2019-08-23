class SLLNode:

        def __init__(self, data):
                self.data = data
                self.next = None

        def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "SLLNode object: data={}".format(self.data)

        def getData(self):
                """Return the self.data attribute."""
                return self.data

        def setData(self, new_data):
                """Replace the existing value of the self.data attribute
                with the new_data parameter.
                """
                self.data = new_data

        def getNext(self):
                """Return the self.next attribute."""
                return self.next

        def setNext(self, new_next):
                """Replace the existing value of the self.next attribute
                with the new_next parameter.
                """
                self.next = new_next


class SLL:

        def __init__(self):
                self.head = None

        def __repr__(self):
                return "SLL object: head={}".format(self.head)

        def isEmpty(self):
                return self.head is None  # self.head == None

        def addNode(self, new_data):
                """Add a Node whose data is the new_data argument to the
                front of the Linked List.
                """
                temp = SLLNode(new_data)
                temp.setNext(self.head)
                self.head = temp

        def size(self):
                """Traverses the Linked List and returns the number of nodes
                in the Linked List.
                """
                size = 0
                if self.head is None:
                        return 0

                current = self.head
                while current is not None:    # While there are still nodes left to count
                        size += 1
                        current = current.getNext()

                return size

        def search(self, data):
                """Traverses the Linked List and returns True if the the data searched
                for is present in one of the Nodes. Otherwise, it returns False."""
                if self.head is None:
                        return "Linked List is empty."

                current = self.head
                while current is not None:
                        if current.getData() == data:
                                return True
                        else:
                                current = current.getNext()

                return False

        def remove(self, data):
                """Removes the first occurance of a Node that contains the data argument
                as its self.data variable. Returns nothing.
                """
                if self.head is None:
                        return "Linked List is empty. No Nodes to remove."
                current = self.head
                previous = None
                found = False
                while not found:
                        if current.getData() == data:
                                found = True
                        else:
                                if current.getNext() is None:
                                        return "A Node with given data is not present."

                                else:
                                        previous = current
                                        current = current.getNext()
                if previous is None:
                        self.head = current.getNext()
                else:
                        previous.setNext(current.getNext())

