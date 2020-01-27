# Red Black Tree implementation
Red = 'Red'
Black = 'Black'


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = Red


class RedBlackTree:
    def __init__(self):
        nil_node = Node(0)
        nil_node.color = Black
        self.NIL = nil_node
        self.root = self.NIL

    def insert(self, z):
        y = self.NIL                      # variable for the parent of the added node
        temp = self.root

        while temp != self.NIL:
            y = temp
            if z.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        z.parent = y

        if y == self.NIL:                 # newly added node is root
            self.root = z

        elif z.data < y.data:             # data of child is less than its parent, left child
            y.left = z
        else:
            y.right = z

        z.right = self.NIL
        z.left = self.NIL

        self._rebalance_insert(z)

    def _rebalance_insert(self, z):
        while z.parent.color == Red:
            # z.parent is the left child
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right               # uncle of z

                # case 1
                if y.color == Red:
                    z.parent.color = Black
                    y.color = Black
                    z.parent.parent.color = Red
                    z = z.parent.parent

                # case2 or case3
                else:
                    # case2
                    if z == z.parent.right:
                        z = z.parent                    # marked z.parent as new z
                        self._left_rotate(z)

                    # case3
                    z.parent.color = Black              # made parent black
                    z.parent.parent.color = Red         # made parent red
                    self._right_rotate(z.parent.parent)

            # z.parent is the right child
            else:
                y = z.parent.parent.left                # uncle of z
                if y.color == Red:
                    z.parent.color = Black
                    y.color = Black
                    z.parent.parent.color = Red
                    z = z.parent.parent

                else:
                    if z == z.parent.left:
                        z = z.parent                    # marked z.parent as new z
                        self._right_rotate(z)

                    z.parent.color = Black              # made parent black
                    z.parent.parent.color = Red         # made parent red
                    self._left_rotate(z.parent.parent)

        self.root.color = Black

    def delete(self, z):
        y = z
        x = None
        y_orignal_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._restructure(z, z.right)

        elif z.right == self.NIL:
            x = z.left
            self._restructure(z, z.left)

        else:
            y = self._min(z.right)
            y_orignal_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = z

            else:
                self._restructure(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._restructure(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_orignal_color == Black:
            self._rebalance_delete(x)

    def _rebalance_delete(self, x):
        while x != self.root and x.color == Black:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Red:
                    w.color = Black
                    x.parent.color = Red
                    self._left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == Black and w.right.color == Black:
                    w.color = Red
                    x = x.parent

                else:
                    if w.right.color == Black:
                        w.left.color = Black
                        w.color = Red
                        self._right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = Black
                    w.right.color = Black
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Red:
                    w.color = Black
                    x.parent.color = Red
                    self._right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == Black and w.left.color == Black:
                    w.color = Red
                    x = x.parent

                else:
                    if w.left.color == Black:
                        w.right.color = Black
                        w.color = Red
                        self._left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = Black
                    w.left.color = Black
                    self._right_rotate(x.parent)
                    x = self.root

        x.color = Black

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:       # x is root
            self.root = y
        elif x == x.parent.left:       # x is left child
            x.parent.left = y
        else:                          # x is right child
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:       # x is root
            self.root = y
        elif x == x.parent.right:      # x is right child
            x.parent.right = y
        else:                          # x is left child
            x.parent.left = y
        y.right = x
        x.parent = y

    def _restructure(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _min(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def inorder_traverse(self, n):
        if n != self.NIL:
            self.inorder_traverse(n.left)
            print(n.data)
            self.inorder_traverse(n.right)


if __name__ == '__main__':
    t = RedBlackTree()

    my_list = [10, 20, 30, 100, 90, 80]
    node = []

    for item in my_list:
        node.append(Node(item))

    for e in node:
        t.insert(e)

    a = node[2]
    t.delete(a)

    t.inorder_traverse(t.root)


























