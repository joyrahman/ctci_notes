class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LL:
  def __init__(self):
    self.head = None
  
  def add_node(self,x):
    temp = Node(x)
    if self.head==None:
      self.head = temp
    else:
      runner = self.head
      prev = self.head
      while(runner):
        prev = runner
        runner = runner.next
      prev.next = temp
  def print_ll(self):
    runner = self.head
    while(runner):
      print runner.data
      runner = runner.next


def reverse(head,k):
  if head==None:
    return None

  saveHead = head
  count = 0
  prev = None
  while(count<k and head!=None):
    future = head.next
    head.next = prev
    prev = head
    head = future
  
  if future !=None: 
    saveHead.next = reverse(future,k)
  
  return prev



def main():
  ls = LL()
  ls.add_node('a')
  ls.add_node('b')
  ls.add_node('c')
  ls.add_node('d')
  ls.add_node('e')
  ls.add_node('f')
  ls.add_node('g')
  ls.print_ll()
  print "lets reverse"
  ls.head = reverse(ls.head,3)
  ls.print_ll()


if __name__ == "__main__":
    main()
    

