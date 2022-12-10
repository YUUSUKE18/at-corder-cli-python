n,l = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
  if(a[i]%n==0):
      c += 1

if(c!=n):
    print("No")
else:
    print("Yes")