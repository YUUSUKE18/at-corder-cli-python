S = input()

result = "Yes"

if S.isupper() or S.islower(): result = "No"

if len(set(S))!=len(S): result="No"

print(result)