C = list(map(int, input().split()))
C.sort()

if (C[0]==C[1]==C[2] and C[3]==C[4]):
    print("Yes")
elif(C[0]==C[1] and C[2]==C[3]==C[4]):
    print("Yes")
else:
    print("No")