# Write your code here
import queue
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self):
        if self.containsEdge(v1, v2) is False :
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else: 
            return False
        
    def __str__(self):
        return str(self.adjMatrix)

    # Helper function for BFS traversal
    def __bfs(self, sv, visited):
        q = queue.Queue()  # Create a queue for BFS

        q.put(sv)  # Enqueue the starting vertex 'sv' into the queue
        visited[sv] = True  # Mark 'sv' as visited

        while not q.empty():
            u = q.get()  # Dequeue a vertex 'u' from the queue
            print(u, end=' ')  # Print the vertex 'u'

            # Iterate through all vertices to find neighbors
            for i in range(self.nVertices):
                # Check if there is an edge from 'u' to 'i' and if 'i' is not visited
                if self.adjMatrix[u][i] > 0 and not visited[i]:
                    q.put(i)  # Enqueue 'i' if it's a neighbor of 'u'
                    visited[i] = True  # Mark 'i' as visited

    # Public BFS function to start BFS traversal
    def bfs(self):
        visited = [False for i in range(self.nVertices)]  # Initialize visited array

        for i in range(self.nVertices):
            if not visited[i]:
                # Start BFS from unvisited vertices
                self.__bfs(i, visited)
                
# Main
li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E) :
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)
    
g.bfs()



