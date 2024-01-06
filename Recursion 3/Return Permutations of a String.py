def helper(string,prefix,arr):
    if len(string)==0:
        arr.append(prefix)
        return
    for i in range(len(string)):
        current_char=string[i]
        remaining_char=string[:i]+string[i+1:]
        helper(remaining_char,prefix+current_char,arr)

def permutations(string):
    #Implement Your Code Here
    arr=[]
    prefix=""
    helper(string,prefix,arr)
    return arr


string = input()
ans = permutations(string)
for s in ans:
    print(s)   
