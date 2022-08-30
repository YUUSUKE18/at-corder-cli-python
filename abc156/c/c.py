N = int(input())
X = list(map(int,input().split()))
ans=1000000000000000000000000000

for i in range(1, 101):
    p = 0
    for k in range(N):    
        c = abs(i-X[k])**2
        p+=c
    if ans>p:
        ans=p
print(ans)