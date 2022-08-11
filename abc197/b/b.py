H,W,X,Y = map(int, input().split())

area = []

for i in range(H):
    S=input()
    s=list(S)
    area.append(s)
    
X-=1
Y-=1

result=0

for i in range(1,H):
    if(0<=X-i<H):
        if(area[X-i][Y]=="#"):
            break
        else:
            result+=1

for i in range(1,H):
    if(0<=X+i<H):
        if(area[X+i][Y]=="#"):
            break
        else:
            result+=1

for i in range(1,W):
    if(0<=Y-i<W):
        if(area[X][Y-i]=="#"):
            break
        else:
            result+=1

for i in range(1,W):
    if(0<=Y+i<W):
        if(area[X][Y+i]=="#"):
            break
        else:
            result+=1

result+=1

print(result)