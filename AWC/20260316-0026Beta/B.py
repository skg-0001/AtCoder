N, K = map(int, input().split())
A = list(map(int, input().split()))
tak = 0
aok = 0

for x in A:
  if (tak + x) <= K:
    tak += x
  else:
    aok += x

if tak > aok:
  print("Takahashi")
elif tak == aok:
  print("Draw")
else:
  print("Aoki")
