N, K = map(int, input().split())
A = input().split()
D = N // K
ans = ""
i = 0

for _ in range(D):
  ans += A[i + K - 1] + " "
  i += K
  
print(ans)
