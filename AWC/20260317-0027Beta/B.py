# 1回目

N = int(input())
A = list(map(int, input().split()))

ans = 0
maxpoint = 0

for x in A:
  if x > maxpoint:
    maxpoint = x
    ans += 1
  elif A[ans - 1] <= x <= maxpoint:
    ans += 1

if ans == 1:
  print(-1)
else:
  print(ans)



# 2回目

N = int(input())
A = list(map(int, input().split()))

reverse_ans = 0
maxpoint = 0
i = 0


for _ in range(N):
  if A[-1 - i] >= maxpoint:
    maxpoint = A[-1 - i]
    reverse_ans += 1
  elif A[-(reverse_ans)] <= A[-1 - i] <= maxpoint:
    reverse_ans += 1
  i += 1

if (N - reverse_ans) == 1:
  print(-1)
else:
  print(N - reverse_ans)
  
    
