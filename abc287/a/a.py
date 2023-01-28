n = int(input())
c = 0
for _ in range(n):
    if input() == "For":
        c += 1
print("Yes" if c > n // 2 else "No")