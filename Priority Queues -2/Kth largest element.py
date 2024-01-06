import heapq
def kthLargest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    heapq._heapify_max(lst)
    for i in range(k,0,-1):
        ele=heapq._heappop_max(lst)
    return ele


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)