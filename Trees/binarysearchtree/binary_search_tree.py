# Binary Search Tree (BST)
class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    # Helper function for insertion
    def _insert(self, data, current_node):

        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)

        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

        else:
            print("The value is already present in the tree.")

    def search(self, data):

        if self.root:
            found = self._search(data, self.root)
            if found:
                return True
            else:
                return False

    # Helper function for searching
    def _search(self, data, current_node):

        if data < current_node.data and current_node.left:
            return self._search(data, current_node.left)
        elif data > current_node.data and current_node.right:
            return self._search(data, current_node.right)
        if data == current_node.data:
            return True

    # Method-1: BST property check using inorder print
    def inorder_bst(self):

        if self.root:
            self._inorder_bst(self.root)

    # Helper function for bst property check
    def _inorder_bst(self, current_node):

        if current_node:
            self._inorder_bst(current_node.left)
            print(str(current_node.data))
            self._inorder_bst(current_node.right)

    # Method-2: BST property check by comparing nodes
    def is_bst(self):

        if self.root:
            bst_satisfied = self._is_bst(self.root, self.root.data)

            if bst_satisfied is None:
                return True
            return False

        return True

    # Helper function for bst check (is_bst)
    def _is_bst(self, current_node, data):

        if current_node.left:
            if data > current_node.left.data:
                return self._is_bst(current_node.left, current_node.left.data)
            else:
                return False

        if current_node.right:
            if data < current_node.right.data:
                return self._is_bst(current_node.right, current_node.right.data)
            else:
                return False

    def min(self):

        if self.root:
            return self._min(self.root)

    def _min(self, current_node):

        if current_node.left:
            return self._min(current_node.left)

        return current_node.data

    def max(self):

        if self.root:
            return self._max(self.root)

    def _max(self, current_node):

        if current_node.right:
            return self._max(current_node.right)

        return current_node.data

    def delete_node(self, data):

        if self.root is None:
            return self.root
        else:
            return self._delete_node(self.root, data)

    def _delete_node(self, current_node, data):

        # If the data to be deleted is smaller than the root's or current_node's
        # data then it lies in left subtree
        if data < current_node.data:
            current_node.left = self._delete_node(current_node.left, data)

        # If the data to be delete is greater than the root's or current_node's data
        # then it lies in right subtree
        elif data > current_node.data:
            current_node.right = self._delete_node(current_node.right, data)

        # If data is same as current_node's data, then this is
        # the node to be deleted
        else:

            # case-1: Node with no child or 1 child
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp

            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp

            # case-2: Node with 2 child
            else:
                temp = self._min(current_node.right)
                current_node.data = temp
                current_node.right = self._delete_node(current_node.right, temp)

        return current_node


if __name__ == "__main__":

    bst = BST()
    bst.insert(8)
    bst.insert(14)
    bst.insert(5)
    bst.insert(11)
    bst.insert(6)
    bst.insert(3)
    print(bst.search(10))
    bst.insert(11)

    tree = BST()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("\nBST property check: ")
    bst.inorder_bst()
    print("\n")
    tree.inorder_bst()
    print("\n")
    print(bst.is_bst())
    print(tree.is_bst())
    print("\n")
    print("Min of BST: " + str(bst.min()) + "\n")
    print("Max of BST: " + str(bst.max()) + "\n")
    bst.delete_node(6)
    print("Max of BST: " + str(bst.max()) + "\n")
    bst.inorder_bst()




