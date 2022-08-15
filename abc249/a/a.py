A,B,C,D,E,F,X = map(int, input().split())

tak = A*B+C
aok = D*E+F

takAdd = 0
aokAdd = 0
if(X-(A+C)>0):
    tak += (X-(A+C))*B

if(X-(D+F)>0):
    aok += (X-(D+F))*E

if(tak>aok):
    print("Takahashi")
elif(tak<aok):
    print("Aoki")
else:
  	print("Draw")

