## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
## a, b = input().split()
## a = int(a)
## b = int(b)
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)



a,b=input().split()
a=int(a)
b=int(b)
print(power(a,b))