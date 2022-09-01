N, A, B = map(int, input().split())
S = list(input())
 
total = A+B
join = 0
passing = 0
 
for i in range(0,N):
    if S[i]=="a":
        if join < total:
            print("Yes")
            join +=1
        else:
            print("No")
    elif S[i]=="b":
        if join < total and passing < B:
            print("Yes")
            join = join + 1
            passing = passing + 1
        else:
            print("No")
    else:
        print("No")