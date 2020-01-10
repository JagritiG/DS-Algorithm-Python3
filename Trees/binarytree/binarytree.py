# Binary tree implementation
# Tree traversal: breadth-first and depth-first approach
# Breadth-first approach: In-order, pre-order, and post-order traversal
# Depth-first approach: level-order traversal


# Stack class
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item or top item from the list."""

        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """Returns the last or top item in th list."""
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """Returns the length of the list."""
        return len(self.items)

    def is_empty(self):
        """Returns True if list is empty. Else, returns False."""
        return self.items == []

    def pop_all(self):
        """Remove all the elements from a stack recursively."""
        if self.items:
            self.pop()
            return self.pop_all()


# Queue class
class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def first(self):
        if self.items:
            return self.items[-1].val

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


# A class that represents an individual node in a Binary Tree
class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.root)

    def tree_print(self, traversal_type):

        if traversal_type == "inorder":
            return self.in_order(self.root, "")

        if traversal_type == "preorder":
            return self.pre_order(self.root, "")

        if traversal_type == "postorder":
            return self.post_order(self.root, "")

        if traversal_type == "levelorder":
            return self.level_order(self.root)

        if traversal_type == "revlevelorder":
            return self.rev_level_order(self.root)

# A function to do inorder tree traversal
    def in_order(self, start, traversal):
        """Left->Root->Right"""
        if start:

            # first perform recursion on left child
            traversal = self.in_order(start.left, traversal)

            # Then get the data of the node
            traversal += (str(start.val) + " ")

            # Then perform recursion on right child
            traversal = self.in_order(start.right, traversal)

        return traversal

    # A function to do preorder tree traversal
    def pre_order(self, start, traversal):
        """Root->Left->Right"""
        if start:

            # first get the data of the node
            traversal += (str(start.val) + " ")

            # Then perform recursion on left child
            traversal = self.pre_order(start.left, traversal)

            # Then perform recursion on right child
            traversal = self.pre_order(start.right, traversal)

        return traversal

    # A function to do postorder tree traversal
    def post_order(self, start, traversal):
        """Left->Right->Root"""
        if start:

            # first perform recursion on left child
            traversal = self.post_order(start.left, traversal)

            # Then perform recursion on right child
            traversal = self.post_order(start.right, traversal)

            # Then get the data of the node
            traversal += (str(start.val) + " ")

        return traversal

    # A function to do level order tree traversal
    def level_order(self, start):

        if not start:
            return

        q = Queue()
        q.enqueue(start)

        traversal = ""
        while len(q) > 0:

            traversal += str(q.first()) + " "
            node = q.dequeue()

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return traversal

    # A function to do reverse level order tree traversal
    def rev_level_order(self, start):

        if not start:
            return

        q = Queue()
        s = Stack()
        q.enqueue(start)

        traversal = ""
        while len(q) > 0:
            node = q.dequeue()
            s.push(node)

            if node.right:
                q.enqueue(node.right)
            if node.left:
                q.enqueue(node.left)

        while s.size():
            node = s.pop()
            traversal += str(node.val) + " "
        return traversal

    def height(self, node):

        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_iter(self):

        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack.size():
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size

    def size_rcur(self, node):

        if node is None:
            return 0

        return 1 + self.size_rcur(node.left) + self.size_rcur(node.right)


if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    print("Inorder print: ")
    print(tree.tree_print("inorder") + "\n")
    print("Preorder print: ")
    print(tree.tree_print("preorder") + "\n")
    print("Postorder print: ")
    print(tree.tree_print("postorder") + "\n")
    print("Levelorder print: ")
    print(tree.tree_print("levelorder") + "\n")
    print("reverseLevelorder print: ")
    print(tree.tree_print("revlevelorder") + "\n")
    print("Height of the binary tree: " + str(tree.height(tree.root)) + "\n")
    print("Size of the tree: " + str(tree.size_iter()) + "\n")
    print("Size of the tree: " + str(tree.size_rcur(tree.root)))

#       1
#     /   \
#   2       3
#  / \     /
# 4   5   6

# Pre-order:     1 2 4 5 3 6     ; (Root->Left->Right)
# In-order:      4 2 5 1 6 3     ; (Left->Root->Right)
# Post-order:    4 5 2 6 3 1     ; (Left->Right->Root)
# Level-order:   1 2 3 4 5 6
# Reverse Level-order: 4 5 6 2 3 1
# Height of the binary tree: 2
# Size of the tree: 6


