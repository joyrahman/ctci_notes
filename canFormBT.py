'''
* Definition for a binary tree node. 
* public class TreeNode { 
* int val; 
* TreeNode left; 
* TreeNode right; 
* TreeNode(int x) { val = x; } 
* } 
Given an array of Binary Tree Node, check if all of these nodes can form a binary tree? 
Public boolean canForm(TreeNode[] nodes){ 
}


'''
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def canForm(nodes):
    parents = dict() # child -> parent relationship, a child should appear at most once
    for node in nodes:
        if node.left is not None:
            if node.left in parents:
                return False
            parents[node.left] = node
            
        if node.right is not None:
            if node.right in parents:
                return False
            parents[node.right] = node
            
    return len(parents) == len(nodes) - 1

