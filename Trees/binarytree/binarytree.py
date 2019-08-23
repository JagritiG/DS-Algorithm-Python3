class BinaryTree:

    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def __repr__(self):
                return "BinaryTree object: node={}".format(self.root)

    def insertLeftChild(self, node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(node)

        else:
            t = BinaryTree(node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRoot(self):
        return self.root

    def setRoot(self, r):
        self.root = r

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
















