#code

# todo things 
from collections import defaultdict

class Node :
    def __init__(self,id):
        self.id = id
        self.addList = []

class Graph():
    def __init__(self,n):
        self.vertices = n 
        self.graph = defaultdict(list)
    
    
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    
    def union(self,parent, a, b):
        x_set = self.find_parent (parent, a)
        y_set = self.find_parent (parent, b)
        parent[x_set] = y_set
        
    
    def find_parent(self, parent, item):
        if parent[item] == -1:
            return item 
        if parent[item ] != -1:
            return self.find_parent(parent, parent[item])
    
    def isCyclic(self):
        parent = [ -1 ] * self.vertices
        
        for u in self.graph:   #for each node 
            for v in self.graph[u]:  # for each neighbor of adj list 
                x = self.find_parent( parent, u)
                y = self.find_parent( parent, v)
                if (x==y):
                    
                    return True
                self.union(parent,u,v)



g = Graph(3)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)

if g.isCyclic()==True:
    print "Cycle present"
else: 
    print "No Cycle"




'''
(0) -----------------------> (1)
    <--\                    /
        \                  /  
        \-----------(2)<-/


'''


 
