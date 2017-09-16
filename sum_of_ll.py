class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.capacity = 0

    def addNode(self,n):
        # case1 : empty list
        if self.head == None:
            self.head = n
        # case2 : non empty list
        else:
            runner = self.head
            prev = None
            while(runner):
                prev = runner
                runner = runner.next
            prev.next = n
        # increase the size
        self.capacity += 1

    def printList(self):
        runner  = self.head
        while runner:
            print runner.data,"-> ",
            runner = runner.next
        print ""



def sum_of_ll( ll1, ll2 ):
    result = LL()
    carry = 0
    list1 = ll1.head
    list2 = ll2.head

    while ((list1 != None) or (list2!= None)):
        #case list1 empty
        if list1 == None:
            temp = (list2.data + carry) % 10
            carry = (list2.data + carry) / 10
            list2 = list2.next

        elif list2 == None:
            temp = (list1.data + carry) % 10
            carry = (list1.data + carry) / 10
            list1 = list1.next
        #both non empty
        else:
            temp = (list1.data + list2.data + carry)%10 
            carry = (list1.data + list2.data + carry)/10
            list1 = list1.next
            list2 = list2.next
        #create the Node
        tempNode  = Node(temp)
        result.addNode(tempNode)

    return result



def main():
    list1 = LL()
    list1.addNode(Node(5))
    list1.addNode(Node(4))
    list1.printList()

    list2 = LL()
    list2.addNode(Node(5))
    list2.addNode(Node(4))
    list2.addNode(Node(3))
    list2.printList()

    result = sum_of_ll(list1, list2)
    result.printList()

if __name__ == "__main__":
    main()
