def helper(str,index,n,result,arr):
    if index==n:
        arr.append(result)
    else:
        helper(str,index+1,n,result+str[index],arr)
        helper(str,index+1,n,result,arr)
def subsequences(string):
    #Implement Your Code Here
    index=0
    n=len(string)
    result=""
    arr=[]
    helper(string,index,n,result,arr)
    asd=list()
    for ele in arr:
        if ele!="":
            asd.append(ele)
    return asd
    


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)