#IsBST()
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:
The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Ref:[isBST](https://www.hackerrank.com/challenges/ctci-is-binary-search-tree)

```python
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys
def check_binary_search_tree_(root,lMin=None,lMax=None):
    if root==None:
        return True
    
    if lMin==None and lMax==None:
        lMin = -sys.maxint-1;
        lMax = sys.maxint;
    
    if root.data <=  lMin or root.data>= lMax:
        return False
    return check_binary_search_tree_(root.left,lMin,root.data) and check_binary_search_tree_(root.right,root.data,lMax)
```
