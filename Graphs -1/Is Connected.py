# Write your code here
from sys import stdin
import queue
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.matrix=[[0]*vertices for i in range(self.vertices)]
    def add_edges(self,v1,v2):
        self.matrix[v1][v2]=1
        self.matrix[v2][v1]=1
    def __BFS(self):
        visited=[False for i in range(self.vertices)]
        q=queue.Queue()
        q.put(0)
        visited[0]=True
        ans=list()
        while q.empty() is False:
            ele=q.get()
            ans.append(ele)
            for i in range(self.vertices):
                if self.matrix[ele][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
        return ans

    def BFS(self):
        if self.vertices!=0:
            li=[int(x) for x in range(self.vertices)]
            ans=self.__BFS()
            for x in li:
                if x not in ans:
                    return False
            return True
        else:
            return True
li=stdin.readline().strip().split()
V=int(li[0])
E=int(li[1])
G=Graph(V)

for i in range(E):
    arr=stdin.readline().strip().split()
    V1=int(arr[0])
    V2=int(arr[1])
    G.add_edges(V1,V2)
if G.BFS():
    print("true")
else:
    print("false")