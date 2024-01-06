def uniqueChar(s): 
    # Write your code here
    arr=list()
    for i in range(len(s)):
        if s[i] not in arr:
            arr.append(s[i])
    result="".join(str(i)for i in arr)
    return result
    






# Main 
s=input() 
print(uniqueChar(s))