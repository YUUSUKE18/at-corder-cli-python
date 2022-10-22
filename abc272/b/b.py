n, m = map(int, input().split())
array = [list(map(int, input().split())) for i in range(m)]

c = 0
for k in range(n):
    array[k].sort()
    if(array[k][0] == array[k][1] or array[k][1] == array[k][2]):
        c += 1

if c > 0:
    print("Yes")
else:
    print("No")