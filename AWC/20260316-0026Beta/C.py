N, T, E = map(int, input().split())
P = list(map(int, input().split()))

P_min = sorted(P)
A = E / T
i = 0
j = 0

for x in P_min:
  if i + x <= A:
    i += x
    j += 1

print(j)
