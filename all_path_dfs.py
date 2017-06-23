from collections import defaultdict

class Graph:

    def __init__(self,numberVertices):
        self.V = numberVertices
        self.graph  = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):
        # mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # if current vertex is same as destination, print current path[]
        if u == d:
            print path
        else:
            # if current verted is not destinatio, recur for all the vertices
            # adjacent to this verted
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
        # Remove current vertex from path and make it unvisited
        path.pop()
        visited[u] = False



    def printAllPaths(self,s,d):

        # mark all the vertices as not visited
        visited = [False] * (self.V)

        # create an array to store paths
        path = [ ]

        # call the recursive helper function to print all paths

        self.printAllPathsUtil(s, d, visited, path)









g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(1,3)


s = 2; d = 3
print("Following are all different paths from %d to %d:"%(s,d))
g.printAllPaths(s, d)
