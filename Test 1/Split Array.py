


def check(input,size,startIndex,lSum,rSum):
    if startIndex==size:
        return lSum==rSum
    if input[startIndex]%5==0:
        lSum+=input[startIndex]
    elif input[startIndex]%3==0:
        rSum+=input[startIndex]
    else:
        left_ans=check(input,size,startIndex+1,lSum+input[startIndex],rSum)
        right_ans=check(input,size,startIndex+1,lSum,rSum+input[startIndex])
        return left_ans or right_ans
    return check(input,size,startIndex+1,lSum,rSum)
def split_array(input, size):
    # write your code here !!
    return check(input,size,0,0,0)







    

def main():
    size = int(input())
    input_array = list(map(int, input().split()))

    if split_array(input_array, size):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
