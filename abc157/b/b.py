## ビンゴカードの配列作成
bingo = [list(map(int, input().split())) for i in range(3)]

## 数値入力
n = int(input())
## 入力された数値の確認(Loop処理)
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == b:
                bingo[i][j] = -1

for i in range(3):
    if bingo[i][0] == bingo[i][1] == bingo[i][2] == -1:
        print("Yes")
        exit()
    elif bingo[0][i] == bingo[1][i] == bingo[2][i] == -1:
        print("Yes")
        exit()
    elif bingo[0][0] == bingo[1][1] == bingo[2][2] == -1:
        print("Yes")
        exit()
    elif bingo[0][2] == bingo[1][1] == bingo[2][0] == -1:
        print("Yes")
        exit()
    else:
        print("No")
        exit()