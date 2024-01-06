# Write your code here...
def string_conversion(string,n):
    if n==0:
        return int(string[n])
    smalloutput=int(string[n])+10*string_conversion(string,n-1)
    return smalloutput





string=input()
print(string_conversion(string,len(string)-1))