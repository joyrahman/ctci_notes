# https://www.hackerrank.com/contests/w33/challenges/bonnie-and-clyde
import sys
from collections import defaultdict

class Graph:

    def __init__(self,numberVertices):
        self.V = numberVertices
        self.graph  = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, w, visited, path,origin,result):
        # mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # if current vertex is same as destination, print current path[]
        if u == d:
            #print "{} {} {} > {}".format(origin,d,w,path)
            if w in path:
                result.append(1)
                return
        else:
            # if current verted is not destinatio, recur for all the vertices
            # adjacent to this verted
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, w, visited, path,origin,result)
        # Remove current vertex from path and make it unvisited
        path.pop()
        visited[u] = False



    def printAllPaths(self,s,d,w,result):

        # mark all the vertices as not visited
        visited = [False] * (self.V+1)

        # create an array to store paths
        path = [ ]

        # call the recursive helper function to print all paths

        self.printAllPathsUtil(s, d, w, visited, path,s, result)









#s = 2; d = 3
#print("Following are all different paths from %d to %d:"%(s,d))
#g.printAllPaths(s, d)



n, m, q = raw_input().strip().split(' ')
n, m, q = [int(n), int(m), int(q)]

g = Graph(n)
for a0 in xrange(m):
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]
    g.addEdge(u,v)
    g.addEdge(v,u)

for a0 in xrange(q):
    u, v, w = raw_input().strip().split(' ')
    u, v, w = [int(u), int(v), int(w)]
    result = []
    g.printAllPaths(u,v,w,result)
    if result == []:
        print "NO"
    else:
        print "YES"


