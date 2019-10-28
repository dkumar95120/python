class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 

    def print(self):
        if self.left:
            self.left.print()
        print(self.info)
        if self.right:
            self.right.print()
        return

    def depth(self, h=0):
        hl = hr = h
        if bool(self.left):
            hl = self.left.depth(h+1)
        if bool(self.right):
            hr = self.right.depth(h+1)
        return max(hl,hr)

def invert(root):
    # base case if tree is empty
    if root == None:
        return

    # swap left subtree with right subtree
    root.left, root.right = root.right, root.left

    # invert left subtree
    invert(root.left)

    # invert right subtree
    invert(root.right)

class Tree:
    def __init__(self):
        self.head = None

#  this is a node of the tree , which contains info as data, left , right

# print function to echo tree contents        
    def print(self):
        if bool(self.head):
            self.head.print()

# depth function to compute tree depth
    def depth(self):
        h = 0
        if bool(self.head):
            h = self.head.depth(0)

        return h

    
# reverse function
    def reverse(self):
        invert(self.head)


def insert(root, node):
    if root is None: 
        root = node 
    else: 
        if root.info < node.info: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
    return root