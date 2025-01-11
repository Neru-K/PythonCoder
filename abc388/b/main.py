N, D = map(int, input().split())

T = []
L = []

for i in range(N):
  t, l = map(int, input().split())
  T.append(t)
  L.append(l)

for k in range(1, D + 1):
  maxW = 0

  for j in range(N):
    W = T[j] * (L[j] + k)
    if W > maxW:
      maxW = W

  print(maxW)