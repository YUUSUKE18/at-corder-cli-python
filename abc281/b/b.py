S = input()
flag = True

if len(S) != 8 or S[0].isdigit() or S[7].isdigit():
    flag = False
elif not S[1:7].isdecimal() or S[1] == '0':
    flag = False

if(flag==True):
    print("Yes")
else:
    print("No")