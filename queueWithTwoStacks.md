#Implement Queue using two stacks with amortized cost of pop O(1)
```python
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        return self.second[-1]
        
    def pop(self):
        self.peek()
        return self.second.pop()
    
    def put(self, value):
        self.second.append(value)
        
queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
```
