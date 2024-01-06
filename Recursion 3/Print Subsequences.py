## Read input as specified in the question.
## Print output as specified in the question.
def print_subsequence(str,index,n,result):
    if index==n:
        print(result)
        return
    else:
        print_subsequence(str,index+1,n,result+str[index])
        print_subsequence(str,index+1,n,result)



string=input()
index=0
result=""
n=len(string)
print_subsequence(string,index,n,result)