## Read input as specified in the question.
## Print output as specified in the question.
import sys
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.matrix=[[0]*self.vertices for i in range(self.vertices)]
    def Add_edge(self,v1,v2,wt):
        self.matrix[v1][v2]=wt
        self.matrix[v2][v1]=wt
    def get_mini_vertex(self,visited,weight):
        min_vertex=-1
        max_weight=float("inf")
        for i in range(self.vertices):
            if visited[i] is False and weight[i]<max_weight:
                min_vertex=i
                max_weight=weight[i]
        return min_vertex

        
    def Prim_algo(self):
        visited=[False for i in range(self.vertices)]
        parent=[-1 for i in range(self.vertices)]
        weight=[float('inf') for i in range(self.vertices)]
        parent[0]=-1
        weight[0]=0
        for i in range(self.vertices-1):
            u=self.get_mini_vertex(visited,weight)
            visited[u]=True
            for j in range(self.vertices):
                if visited[j] is False and  self.matrix[u][j]>0 and weight[u]!=float("inf") and ( weight[u]+self.matrix[u][j]<weight[j]):
                    weight[j]=weight[u]+self.matrix[u][j]

                    parent[i]=u
        for i in range(self.vertices):
                print(str(i)+" "+str(weight[i]))

            
li=[int(x) for x in input().split()]
V=int(li[0])
E=int(li[1])
G=Graph(V)
for i in range(E):
    arr=[int(x) for x in input().split()]
    G.Add_edge(arr[0],arr[1],arr[2])
G.Prim_algo()

