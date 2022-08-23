N = int(input())

day = 1
count= 0
while True:
    count += day
    if(count >= N):
        break
    else:
        day += 1

print(day)