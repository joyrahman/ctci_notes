"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""
def findLength(head):
    count = 0
    while(head):
        head = head.next
        count += 1
        
    return count

def FindMergeNode2(headA, headB):
    l1 = findLength(headA)
    l2 = findLength(headB)
    
    if l1>l2:
        # do this
        count = l1-l2
        while(count):
            headA = headA.next
            count -= 1
    else:
        count = l2-l1
        while(count):
            headB = headB.next
            count -=1 
    
    
    while (headA or headB):
        #break
        if headA.data == headB.data:
            return headA.data
        else:
            headA = headA.next
            headB = headB.next
            
  
def FindMergeNode(headA, headB):
    curA = headA
    curB = headB 
    
    while (not curA == curB):
        if  curA.next is None:
            curA = headB
        else:
            curA = curA.next
        
        if  curB.next is None:
            curB = headA
        else:
            curB = curB.next
        
    return curB.data
