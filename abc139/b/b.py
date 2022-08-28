A, B = map(int, input().split())

c = 1
sum = A

if B ==1:
    print(0)
else:
    while sum < B:
        c +=1
        sum += A-1
    print(c)