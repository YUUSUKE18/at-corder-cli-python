n = int(input())
array = list(map(int, input().split()))

sum = 0

for i in range(n):
  sum += array[i]
  
print(sum)