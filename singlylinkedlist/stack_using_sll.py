# Implementing a Stack with a Singly Linked List.
# Orient the top of the stack at the head of the list.


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    # ---------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'           # streamline memory usage

        def __init__(self, element, next):        # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

    # ---------------- stack methods ----------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None                         # reference to the head node
        self._size = 0                            # number of stack elements

    def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "{}".format(self._head)

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)     # create and link a new node
        self._size += 1

    def top(self):
        """Return the element at the top of the stack without removing.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element                 # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        result = self._head._element
        self._head = self._head._next              # bypass the former top node
        self._size -= 1
        return result


if __name__ == "__main__":
    stk = LinkedStack()
    print(stk.is_empty())
    stk.push(2)
    stk.push(3)
    stk.push(4)
    print(stk.top())
    stk.pop()
    print(stk.top())



