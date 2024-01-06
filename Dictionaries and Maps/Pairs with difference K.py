def printPairDiffK(l, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pairs=0
    d=dict()
    for num in l:
        if num in d:
            d[num]=d[num]+1
        else:
            d[num]=1
    for num in d:
        if k==0:
            pairs+=d[num]*(d[num]-1)//2
        else:
            if num+k in d:
                pairs+=d[num]*d[num+k]
    return pairs


    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))