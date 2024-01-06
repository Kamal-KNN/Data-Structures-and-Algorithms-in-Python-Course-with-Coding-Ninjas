class Edge:
    def __init__(self,src,dst,weight):
        self.src=src
        self.dst=dst
        self.weight=weight

def getfind(v,parent):
    if v==parent[v]:
        return v
    return getfind(parent[v],parent)
def krusakl_algorithm(edges,V):
    parent=[ int(i) for i in range(V)]
    edges=sorted(edges,key=lambda edge:edge.weight)
    count=0
    i=0
    output=[]
    while count<(V-1):
        current_element=edges[i]
        V1=getfind(current_element.src,parent)
        V2=getfind(current_element.dst,parent)
        if V1!=V2:
            output.append(current_element)
            parent[V1]=V2
            count+=1
        i+=1
    return output
li=input().split()
N=int(li[0])
E=int(li[1])
edges=[]
for i in range(E):
    arr=[int(x) for x in input().split()]
    src=arr[0]
    dst=arr[1]
    weight=arr[2]
    kamal=Edge(src,dst,weight)
    edges.append(kamal)
        


output=krusakl_algorithm(edges,N)
for edge in output:
    if edge.src<edge.dst:
        print(str(edge.src)+" "+str(edge.dst)+" "+str(edge.weight))
    else:
        print(str(edge.dst)+" "+str(edge.src)+" "+str(edge.weight))
    


