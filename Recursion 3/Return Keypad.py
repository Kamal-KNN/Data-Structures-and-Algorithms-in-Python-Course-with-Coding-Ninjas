
def keypad(n):
    #Implement Your Code Here
    if not n :
        return []
    key={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
        
        
    }
    def backtracking(combination,next_digit):
        if not next_digit:
            result.append(combination)
            return
        current_digit=next_digit[0]
        letters=key[current_digit]
        for letter in letters:
            backtracking(combination+letter,next_digit[1:])
        
    result=[]
    n=str(n)
    backtracking("",n)
    return result

    

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)