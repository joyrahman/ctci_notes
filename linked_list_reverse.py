class Node:
  def __init__(self,x):
    self.data = x
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

  def reverse(self):
    prev = None
    runner = self.head
    while(runner):
      next_node = runner.next    # n:C |  B-->C
      runner.next = prev   # change from A<--B
      prev = runner
      runner  = next_node
    self.head = prev
  def print_ll(self):
    runner = self.head
    while(runner):
      print runner.data
      runner = runner.next


def main():
  ls = LL()
  ls.add_node(1)
  ls.add_node(2)
  ls.add_node(3)
  ls.add_node(4)
  ls.add_node(5)
  ls.print_ll()
  print "lest reverse"
  ls.reverse()
  ls.print_ll()


if __name__ == "__main__":
    main()
