class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
           

#  this is a node of the tree , which contains info as data, left , right
    def insert(self, node):
        if self.info > node.info:
            if bool(self.left):
                self.left.insert(node)
            else:
                self.left = node
        elif self.info < node.info:
            if bool(self.right):
                self.right.insert(node)
            else:
                self.right = node
        else:
            print('Pre-existing')
        return

# print function to echo tree contents        
    def print(self):
        if bool(self.left):
            self.left.print()
        print(self.info)
        if bool(self.right):
            self.right.print()
        return

# depth function to compute tree depth
    def depth(self, h):
        hl = hr = h
        if bool(self.left):
            hl = self.left.depth(h+1)
        if bool(self.right):
            hr = self.right.depth(h+1)
        return max(hl,hr)

def getNode (cur, value):
    if cur == None:
        return None

    if cur.info == value:
        return cur

    node = getNode(cur.left, value)
    if node != None:
        return node

    node = getNode(cur.right, value)
    if node != None:
        return node

    return None

def getPath(root, value):
    if root == None:
        return []

    if root.info == value:
        return [root.info]

    res = getPath(root.left, value)

    if bool(res):
        return [root.info] + res

    res = getPath(root.right, value)
    if bool(res):
        return [root.info] + res

    return []

def LCA (root, val1, val2):
    if root == None:
        return None
    path1 = getPath(root, val1)
    path2 = getPath(root, val2)
    lp = min(len(path1), len(path2))
    for i in range(lp):
        if path1[i] != path2[i]:
            break
    return path1[max(i-1,0)]

def lca (cur, v1, v2):
  #For BST the problem the lca value must be between v1 and v2
    if cur == None:
        return None
    while True:
        if (cur and cur.info > v1 and cur.info > v2):
            cur = cur.left
        elif (cur and cur.info < v1 and cur.info < v2):
            cur = cur.right
        else:
            break
    return cur

