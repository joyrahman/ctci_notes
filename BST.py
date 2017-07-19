class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def get(self):
        return self.val

    def set(self,val):
        self.val = val

    def getChildren(self):
        children = []

        if self.left !=None:
            children.append(self.left)
        if self.right != None:
            children.append(self.right)

        return children



class BST: 
    def __init__(self):
        self.root = None

    def setRoot(self,val):
        self.root = Node(val)

    def insert(self, val):
        if self.root == None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.val:
            if  currentNode.left:
                self.insertNode(currentNode.left, val)
            else:
                currentNode.left = Node(val)
        elif val > currentNode.val:
            if currentNode.right:
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)

    def inorder(self, currentNode):
        if currentNode == None:
            return

        self.inorder(currentNode.left)
        print currentNode.val
        self.inorder(currentNode.right)

    def inorderIterative(self, currentNode):
        s = []

        while ( s!=[] or currentNode != None):
            if currentNode!=None:
                s.append(currentNode)
                currentNode = currentNode.left
            else:
                t = s.pop()
                print t.val
                currentNode = t.right

    def kthSmallest(self, currentNode, k ):
        s = []
        result = 0
        while ( s!=[] or currentNode != None):
            if currentNode!=None:
                s.append(currentNode)
                currentNode = currentNode.left
            else:
                t = s.pop()
                k -= 1
                if k==0:
                    result = t.val
                currentNode = t.right

        
        return result



bst = BST()
data = [4,8,12,10,14,22,20]
for item in data:
    bst.insert(item)
bst.inorder(bst.root)
bst.inorderIterative(bst.root)
print bst.kthSmallest(bst.root,3)
