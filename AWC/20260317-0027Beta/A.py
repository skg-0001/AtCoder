N, S, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for x in A:
  if (S - T) <=  x <=  (S + T):
    ans += 1


print(ans)
