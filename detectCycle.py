from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def isCyclicUtil(self, v, visited, recStack):
        pass




    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V


