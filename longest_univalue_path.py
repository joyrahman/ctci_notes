class Node:
    def __init__(self,n):
        self.value = n
        self.left = None
        self.right = None

class BTree:
    def __init__(self,n):
        self.root = Node(n)

    def addNode(self,n):

        def addNodeHelper(cur_root,n):
            if cur_root == None:
                cur_root = Node(n)
            elif n < cur_root.value:
                if cur_root.left:
                    addNodeHelper( cur_root.left,n)
                else:
                    cur_root.left = Node(n)
            else:
                if cur_root.right:
                    addNodeHelper( cur_root.right, n)
                else:
                    cur_root.right = Node(n)

        addNodeHelper(self.root,n)

    def traversal(self):

        def traversal_helper(cur_root):
            print (cur_root.value)
            if cur_root.left:
                traversal_helper(cur_root.left)
            if cur_root.right:
                traversal_helper(cur_root.right)

        traversal_helper(self.root)



class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0


        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)

            left_val = right_val = 0
            
            #check left side exist and of same value
            if node.left and node.left.value == node.value:
                left_val = left_length + 1
            #check right side exist and of same value
            if node.right and node.right.value == node.value:
                right_val = right_length + 1
            
            self.ans =  max (self.ans, right_val + left_val)
            return max(left_val, right_val)


        arrow_length(root)
        return self.ans




def main():
    bt = BTree(5)
    bt.addNode(4)
    bt.addNode(5)
    bt.addNode(1)
    bt.addNode(1)
    bt.addNode(5)
    bt.traversal()
    s = Solution()
    print(s.longestUnivaluePath(bt.root))



if __name__ == "__main__":
    main()
