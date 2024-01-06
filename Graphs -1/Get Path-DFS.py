# Write your code here

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
import queue

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.matrix=[[0]*self.vertices for i in range(self.vertices)]
    def add_edges(self,v1,v2):
        self.matrix[v1][v2]=1
        self.matrix[v2][v1]=1
    def __str__(self):
        return self.matrix
    def __BFS_helper(self,visited,i):
        q=queue.Queue()
        q.put(i)
        visited[i]=True
        while q.empty() is False:
            ele=q.get()
            print(ele,end=" ")
            for i in range(self.vertices):
                if self.matrix[ele][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
    def BFS(self,v1,v2):
        visited=[False for i in range(self.vertices)]
        for i in range(self.vertices):
            if visited[i] is False:
                self.__BFS_helper(visited,i)
    def __DFS_PATH_HELPER(self,v1,v2,visited):
        if v1==v2:
            return list([v1])
        visited[v1]=True
        for i in range(self.vertices):
            if self.matrix[v1][i]>0 and visited[i] is False:
                li=self.__DFS_PATH_HELPER(i,v2,visited)
                if li !=None:
                    li.append(v1)
                    return li
        return None
    def get_path_DSF(self,v1,v2):
        visited=[False for i in range(self.vertices)]
        return self.__DFS_PATH_HELPER(v1,v2,visited)
  
        

li=stdin.readline().strip().split()
V=int(li[0])
E=int(li[1])
G=Graph(V)
for i in range(E):
    li=stdin.readline().strip().split()
    v1=int(li[0])
    v2=int(li[1])
    G.add_edges(v1,v2)
arr=stdin.readline().strip().split()
v1=int(arr[0])
v2=int(arr[1])

kamal=G.get_path_DSF(v1,v2)
if kamal !=None:
    print(*kamal)