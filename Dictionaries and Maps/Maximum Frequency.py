# Read input as sepcified in the question
# Print output as specified in the question
N=int(input())
arr=input().split()
d=dict()
for i in arr:
    d[i]=d.get(i,0)+1
maxi=max(d.values())
for i in arr:
    if d[i]==maxi:
        print(i)
        break
