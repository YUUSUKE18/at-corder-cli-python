## ビンゴカードの配列作成
dp = []

for i in range(3):
    tmp = list(map(int, input().split()))
    dp.append(tmp)
n = int(input())
lst = [[False]*3 for i in range(3)]
 
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if dp[j][k]==b:
                lst[j][k]=True
 
for i in range(3):
    if lst[i].count(True)==3:
        print('Yes')
        exit()
for i in range(3):
    if lst[0][i]==True and lst[1][i] ==True and lst[2][i]:
        print('Yes')
        exit()
if lst[0][0]==True and lst[1][1]==True and lst[2][2] ==True or lst[0][2]==True and lst[1][1] == True and lst[2][0]==True:
    print('Yes')
    exit()
print('No')
dp = []

for i in range(3):
    tmp = list(map(int, input().split()))
    dp.append(tmp)
n = int(input())
lst = [[False]*3 for i in range(3)]

for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if dp[j][k]==b:
                lst[j][k]=True

for i in range(3):
    if lst[i].count(True)==3:
        print('Yes')
        exit()
for i in range(3):
    if lst[0][i]==True and lst[1][i] ==True and lst[2][i]:
        print('Yes')
        exit()
if lst[0][0]==True and lst[1][1]==True and lst[2][2] ==True or lst[0][2]==True and lst[1][1] == True and lst[2][0]==True:
    print('Yes')
    exit()
print('No')