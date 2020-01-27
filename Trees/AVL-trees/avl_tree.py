# AVL Tree implementation
class TreeNode:
    """AVL Tree Node class."""

    def __init__(self, val=None):
        """Node constructor"""
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.val)


class AVLTree:
    """Implementation of AVL tree."""
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance_factor = 0

    def insert(self, val):
        """Insert new key into node"""

        # Step-1: implement normal BST
        # Initial tree
        if self.node is None:
            self.node = TreeNode(val)
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        # Insert key to the left subtree
        elif val < self.node.val:
            self.node.left.insert(val)

        # Insert key to the right subtree
        elif val > self.node.val:
            self.node.right.insert(val)

        # Exit, key already exists in the tree

        # Re-balance tree if needed
        self.re_balance()

    def re_balance(self):
        """Rebalance tree after inserting or deleting a node

        to maintain AVL balancing strategy.
        """
        # check if we need to rebalance the tree
        # update height
        # balance tree
        self.update_heights(recursive=False)
        self.update_balances(False)

        # if the balance factor remains −1, 0, or +1 then no rotations are necessary.
        while self.balance_factor < -1 or self.balance_factor > 1:
            # Left subtree is larger than right subtree
            if self.balance_factor > 1:

                # LR case
                if self.node.left.balance_factor < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                # LL case
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            # Right subtree is larger than left subtree
            if self.balance_factor < -1:

                # RL case
                if self.node.right.balance_factor > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                # RR case
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """Update tree height.
        Tree height is max height of either left or right subtrees +1
        for root of the tree.
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else:

            self.height = -1

    def update_balances(self, recursive=True):
        """Calculate tree balance factor.
        bf = height(left subtree) - height(right subtree).
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance_factor = self.node.left.height - self.node.right.height
        else:
            self.balance_factor = 0

    # With right rotation, left subtree replaces current root.
    def rotate_right(self):
        """set self as the right subtree of left subtree."""
        new_root = self.node.left.node
        new_left_subtree = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_subtree
        new_root.right.node = old_root

    # With left rotation, right subtree root replaces current root.
    def rotate_left(self):
        """set self as the left subtree of right subtree."""
        new_root = self.node.right.node
        new_left_subtree = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_subtree
        new_root.left.node = old_root

    def delete(self, val):
        """Delete value from the tree."""
        if self.node is not None:
            if self.node.val == val:
                # case 1: value found in leaf node, delete it
                if not self.node.left.node and not self.node.right.node:
                    self.node = None

                # case 2: Node has only one subtree, replace root with that subtree
                # case 2-a: only right subtree present
                elif not self.node.left.node:
                    self.node = self.node.right.node

                # case 2-b: only left subtree present
                elif not self.node.right.node:
                    self.node = self.node.left.node

                else:
                    # Find successor as smallest node in right subtree or
                    # predecessor as largest node in left subtree
                    successor = self.node.right.node
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.val = successor.val

                        # Delete successor from the replaced node right subtree
                        self.node.right.delete(successor.val)

            elif val < self.node.val:
                self.node.left.delete(val)

            elif val > self.node.val:
                self.node.right.delete(val)

            # Re-balance tree
            self.re_balance()

    def inorder_traverse(self):
        """Left -> root -> Right"""
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.val)
        result.extend(self.node.right.inorder_traverse())

        return result


if __name__ == "__main__":

    tree = AVLTree()
    test_list = [4, 6, 7, 8, 9]
    for i in test_list:
        tree.insert(i)

    print(tree.inorder_traverse())
    tree.insert(11)
    print(tree.inorder_traverse())
    tree.insert(2)
    print(tree.inorder_traverse())
    tree.insert(5)
    print(tree.inorder_traverse())

    tree.delete(11)
    print(tree.inorder_traverse())

    tree.delete(7)
    print(tree.inorder_traverse())


# Output:
# [4, 6, 7, 8, 9]
# [4, 6, 7, 8, 9, 11]
# [2, 4, 6, 7, 8, 9, 11]
# [2, 4, 5, 6, 7, 8, 9, 11]
# [2, 4, 5, 6, 7, 8, 9]
# [2, 4, 5, 6, 8, 9]

