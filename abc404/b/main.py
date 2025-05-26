N = int(input())

S = []
T = []

for _ in range(N):
  S.append(input())

for _ in range(N):
  T.append(input())
  
  for col in zip(*S)