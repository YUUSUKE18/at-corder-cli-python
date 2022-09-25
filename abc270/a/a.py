a, b = map(int, input().split())
p = [1,2,4]
ans = set()

for i in p:
    if a-i>=0:
        a-=i
        ans.add(i)
    if b-i>=0:
        b-=i
        ans.add(i)

output = list(ans)
print(sum(output))