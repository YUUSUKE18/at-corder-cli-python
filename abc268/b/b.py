import re

S = input()
T = input()

res = re.match(S,T)

if res:
    print("Yes")
else:
    print("No")