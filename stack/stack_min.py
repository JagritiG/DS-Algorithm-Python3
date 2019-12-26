# Design a stack that has O(1) push, pop and min functions
# This approach uses O(1) time and O(1) extra space.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "Node({})".format(self.data)


class Stack:

    def __init__(self):
        """Create an empty stack."""
        self.head = None
        self.size = 0
        self.minimum = None

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.head)

    def is_empty(self):
        """Return True if the stack is empty."""
        return self.size == 0

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self.size

    def push(self, e):
        """Add element e to the top of the stack."""
        if self.head is None:
            self.head = Node(e)
            self.minimum = e

        elif e < self.minimum:
            temp = (2 * e) - self.minimum
            new_node = Node(temp)
            new_node.next = self.head
            self.head = new_node
            self.minimum = e
        else:
            new_node = Node(e)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        """Remove and return the element from the top of the stack."""
        if self.head is None:
            print("Stack is empty")

        node_removed = self.head.data
        self.head = self.head.next
        if node_removed < self.minimum:
            self.minimum = ((2 * self.minimum) - node_removed)
        self.size -= 1
        return node_removed

    def peek(self):
        """Returns the last or top item in th list."""
        if self.head is None:
            print("Stack is empty")
        else:
            if self.head.data < self.minimum:
                return self.minimum
            else:
                return self.head.data

    def get_min(self):
        if self.head is None:
            return "Stack is empty"
        else:
            return self.minimum


if __name__ == "__main__":

    stack = Stack()

    stack.push(3)
    stack.push(5)
    print(stack.get_min())
    stack.push(2)
    stack.push(1)
    print(stack.get_min())
    stack.pop()
    print(stack.get_min())
    print(stack.peek())
    stack.pop()
    print(stack.get_min())
    print(stack.__len__())




