N = int(input())
ans = ""
i = N

while i > 1:
  ans += str(i) + ","
  i -= 1
  
if i == 1:
  ans += str(i)
  
print(ans)
