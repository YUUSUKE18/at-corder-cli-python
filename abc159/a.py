N, M = map(int, input().split())

ball = [0]*N+[1]*M
count = 0

for i in range(N+M):
    for k in range(i):
        result = ball[i] + ball[k]
        if(result%2==0):
            count += 1

print(count)