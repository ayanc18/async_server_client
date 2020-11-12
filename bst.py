class Node(object):
    def __init__(self, data, client_id):
        self.data = data
        self.client_id = client_id
        self.left = None
        self.right = None

    def insert(self, data, client_id):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data,client_id)
            else:
                self.left = Node(data,client_id)
                return True
        else:
            if self.right:
                return self.right.insert(data,client_id)
            else:
                self.right = Node(data,client_id)
                return True

    def find(self, data):
        if self.data == data:
            return True
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        return False

    def preorder(self, l):
        l.append(self.data)
        if self.left:
            self.left.preorder(l)
        if self.right:
            self.right.preorder(l)
        return l

    def postorder(self, l):
        if self.left:
            self.left.postorder(l)
        if self.right:
            self.right.postorder(l)
        l.append(self.data)
        return l

    def inorder(self, l):
        if self.left:
            self.left.inorder(l)
        l.append(self.data)
        if self.right:
            self.right.inorder(l)
        return l


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data,client_id):
        if self.root:
            return self.root.insert(data, client_id)
        else:
            self.root = Node(data, client_id)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder_traversal(self):
        if self.root:
            return self.root.preorder([])
        else:
            return []

    def postorder_traversal(self):
        if self.root:
            return self.root.postorder([])
        else:
            return []

    def inorder_traversal(self):
        if self.root:
            return self.root.inorder([])
        else:
            return []
