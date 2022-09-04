S = input()
for i in range(0,9):
  if (S[0]== "0") and (S[1]=="0" and S[7]=="0"):
    print("Yes")
    exit()
  elif(S[0]== "0") and (S[2]=="0" and S[9]=="0"):
    print("Yes")
    exit()
  else:
    print("No")
    