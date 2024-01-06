


def printPermutations(string,prefix=""):
    #Implement Your Code Here
    if len(string)==0:
        print(prefix)
        return
    for i in range(len(string)):
        current_character=string[i]
        remainig_char=string[:i]+string[i+1:]
        printPermutations(remainig_char,prefix+current_character)

string = input()
printPermutations(string)




