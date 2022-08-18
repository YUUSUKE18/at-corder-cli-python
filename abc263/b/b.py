N = int(input())
S =[0]+[0]+list(map(int, input().split()))

i = N
c = 1
while S[i] !=1:
    c +=1
    i = S[i]
    
print(c)