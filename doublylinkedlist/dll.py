class DLLNode:

        def __init__(self, data):
                self.data = data
                self.next = None
                self.previous = None

        def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "DLLNode object: data={}".format(self.data)

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

        def getPrevious(self):
                """Return the self.previous attribute."""
                return self.previous

        def setPrevious(self, new_previous):
                """Replace the existing value of the self.previous attribute
                with the new_previous parameter.
                """
                self.previous = new_previous


class DLL:

        def __init__(self):
                self.head = None

        def __repr__(self):
                return "DLL object: head=".format(self.head)

        def isEmpty(self):
                return self.head is None  # self.head == None

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
                for is present in one of the Nodes. Otherwise, it returns False.
                """
                if self.head is None:
                        return "Linked List is empty."

                current = self.head
                while current is not None:
                        if current.getData() == data:
                                return True
                        else:
                                current = current.getNext()

                return False

        def addNode(self, new_data):
                """Add a Node whose data is the new_data argument to the
                front of the Linked List.
                """
                temp = DLLNode(new_data)
                temp.setNext(self.head)

                if self.head is not None:
                        self.head.setPrevious(temp)

                self.head = temp

        def remove(self, data):
                """Removes the first occurance of a Node that contains the data argument
                as its self.data variable. Returns nothing.
                """
                if self.head is None:
                        return "Linked List is empty. No Nodes to remove."

                current = self.head
                found = False
                while not found:
                        if current.getData() == data:
                                found = True
                        else:
                                if current.getNext() is None:
                                        return "A Node with given data is not present."
                                else:
                                        current = current.getNext()

                if current.previous is None:
                        self.head = current.getNext()
                else:
                        current.previous.setNext(current.getNext())
                        current.next.previous(current.getPrevius)


if __name__ == "__main__":

    d = DLL()
    d.addNode(1)
    d.addNode(2)
    d.addNode(3)
    print(d.size())
    print(d.head)
