# Implementation of splay tree
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        temp = None
        current_node = self.root
        while current_node is not None:
            temp = current_node
            if new_node.data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = temp

        if temp is None:
            self.root = new_node
        elif new_node.data < temp.data:
            temp.left = new_node
        else:
            temp.right = new_node

        self._splay(new_node)

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
            self._splay(Node(data))
            return True
        else:
            return None

    def delete(self, data):
        node = Node(data)
        self._splay(node)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root is not None:
            left_subtree.root.parent = None

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root is not None:
            right_subtree.root.parent = None

        if left_subtree.root is not None:
            max_predecessor = left_subtree._max(left_subtree.root)
            left_subtree._splay(max_predecessor)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root

        else:
            self.root = right_subtree.root

    def _max(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def _left_rotate(self, current_node):
        temp = current_node.right
        current_node.right = temp.left
        if temp.left is not None:
            temp.left.parent = current_node

        temp.parent = current_node.parent
        if current_node.parent is None:        # x is root
            self.root = temp

        elif current_node == current_node.parent.left:    # x is left child
            current_node.parent.left = temp

        else:                       # x is right child
            current_node.parent.right = temp

        temp.left = current_node
        current_node.parent = temp

    def _right_rotate(self, current_node):
        temp = current_node.left
        current_node.left = temp.right
        if temp.right is not None:
            temp.right.parent = current_node

        temp.parent = current_node.parent
        if current_node.parent is None:  # x is root
            self.root = temp

        elif current_node == current_node.parent.right:  # x is right child
            current_node.parent.right = temp

        else:                     # x is left child
            current_node.parent.left = temp

        temp.right = current_node
        current_node.parent = temp

    def _splay(self, current_node):
        while current_node.parent is not None:       # node is not root

            # node is child of root, one rotation (zig rotation)
            if current_node.parent is self.root:
                if current_node == current_node.parent.left:
                    self._right_rotate(current_node.parent)
                else:
                    self._left_rotate(current_node.parent)

            else:
                p_node = current_node.parent       # parent node
                gp_node = p_node.parent       # grandparent node

                # both are left children (zig-zig rotation)
                if current_node.parent.left is current_node and p_node.parent.left is p_node:
                    self._right_rotate(gp_node)
                    self._right_rotate(p_node)

                # both are right children (zig-zig rotation)
                elif current_node.parent.right is current_node and p_node.parent.right is p_node:
                    self._left_rotate(gp_node)
                    self._left_rotate(p_node)

                # one is left child and another is right children (zig-zag rotation)
                elif current_node.parent.right is current_node and p_node.parent.left is p_node:
                    self._left_rotate(p_node)
                    self._right_rotate(gp_node)

                # one is left child and another is right children (zig-zag rotation)
                elif current_node.parent.left is current_node and p_node.parent.right is p_node:
                    self._right_rotate(p_node)
                    self._left_rotate(gp_node)

    def inorder_traverse(self, node):
        if node is not None:
            self.inorder_traverse(node.left)
            print(node.data)
            self.inorder_traverse(node.right)


if __name__ == '__main__':
    t = SplayTree()

    t.insert(10)
    t.insert(20)
    t.insert(100)
    t.insert(40)
    t.insert(50)
    t.insert(80)
    t.insert(130)
    t.insert(120)
    t.insert(110)
    t.insert(30)

    t.inorder_traverse(t.root)
    print("\n")
    t.delete(30)
    t.inorder_traverse(t.root)
    print(t.search(30))
    print(t.search(80))
