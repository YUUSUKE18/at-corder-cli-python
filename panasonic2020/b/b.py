h, w = map(int, input().split())

if h == 1 or w == 1:
    c = 1
else:
    c = (h*w+1) //2
print(c)