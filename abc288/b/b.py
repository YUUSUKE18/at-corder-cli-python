n,k = map(int,input().split())
s = [input() for _ in range(n)]
for j in sorted(s[:k]):
  print(j)
