class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "BinaryTree object: val={}".format(self.key)

    def insert_left(self,newNode):
        if self.left_child is None:
            self.left_child = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.left_child = self.left_child
            self.left_child  = t

    def insert_right(self,newNode):
        if self.right_child is None:
            self.right_child = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self,obj):
        self.key = obj

    def get_root_val(self):
        return self.key
