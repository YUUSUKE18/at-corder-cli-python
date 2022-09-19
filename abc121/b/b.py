n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
 
count = 0
for j in range(n):
    a_list = a[j]
    total = 0
    for i in range(m):
        total += a_list[i] * b[i]
    else:
        if total + c > 0:
            count += 1
else:
    print(count)
