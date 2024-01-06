def contains(s,t):
    #Implement This Function Here
    s_pointer=0
    t_pointer=0
    while s_pointer<len(s) and t_pointer<len(t):
        if s[s_pointer]==t[t_pointer]:
            t_pointer=t_pointer+1
        s_pointer=s_pointer+1
    if t_pointer==len(t):
        return True
    else:
        return False


    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')