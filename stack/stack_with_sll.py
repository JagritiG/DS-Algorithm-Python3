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
        __slots__ = 'element', 'next'           # streamline memory usage

        def __init__(self, element, nxt):        # initialize node's fields
            self.element = element               # reference to user's element
            self.next = nxt                     # reference to next node

    # ---------------- stack methods ----------------------------------
    def __init__(self):
        """Create an empty stack."""
        self.head = None                         # reference to the head node
        self.size = 0                            # number of stack elements

    def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "{}".format(self.head)

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self.size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self.size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.head = self._Node(e, self.head)     # create and link a new node
        self.size += 1

    def top(self):
        """Return the element at the top of the stack without removing.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head.element                 # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        result = self.head.element
        self.head = self.head.next              # bypass the former top node
        self.size -= 1
        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.element,)
            current = current.next

    def reverse(self):
        """Reverse a stack using recursion."""
        if not self.head:
            return print("Stack is empty")

        else:
            current = self.head
            prev_node = None
            while current:
                next_node = current.next
                current.next = prev_node
                prev_node = current
                current = next_node
            self.head = prev_node

        return self.head


if __name__ == "__main__":
    stk = LinkedStack()
    print(stk.is_empty())
    stk.push(2)
    stk.push(3)
    stk.push(4)
    # stk.pop()
    # print(stk.top())
    stk.print_list()
    print(stk.top())
    print("\n")
    stk.reverse()
    stk.print_list()
    print(stk.top())
