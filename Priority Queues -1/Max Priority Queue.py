class priorityNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority
class PriorityQueue:
    def __init__(self):
        self.pq=[]
    def isEmpty(self):
        #Implement the isEmpty() function here
        return self.getSize()==0
        
    
    def getSize(self):
        #Implement the getSize() function here
        return len(self.pq)

    def getMax(self):
        #Implement the getMax() function here
        if self.isEmpty() is True:
            return None
        return self.pq[0].value
    def __percolateup(self):
        index=self.getSize()-1
        while index>0:
            parent=(index-1)//2
            if self.pq[index].priority>self.pq[parent].priority:
                self.pq[index],self.pq[parent]=self.pq[parent],self.pq[index]
                index=parent
            else:
                break
        
      
    def insert(self,value,priority):
        #Implement the insert() function here
        node=priorityNode(value,priority)
        self.pq.append(node)
        self.__percolateup()
    def __percolatedown(self):
        parent=0
        left=2*parent+1
        right=2*parent+2
        while left<self.getSize():
            maxindex=parent
            if self.pq[left].priority>self.pq[maxindex].priority:
                maxindex=left
            if right<self.getSize() and self.pq[right].priority>self.pq[maxindex].priority:
                maxindex=right
            if maxindex!=parent:
                self.pq[maxindex],self.pq[parent]=self.pq[parent],self.pq[maxindex]
                parent=maxindex
                left=2*parent+1
                right=2*parent+2
            else:
                break

        
    def removeMax(self):
        #Implement the removeMax() function here
        if self.isEmpty() is True:
            return None
        self.pq[0],self.pq[self.getSize()-1]=self.pq[self.getSize()-1],self.pq[0]
        element=self.pq.pop()
        self.__percolatedown()
        return element.value
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1