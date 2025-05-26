N = int(input())
P = list(map(int, input().split()))
R = [0] * N

for i in range(1, N - 1):
  if P[i - 1] < P[i] and P[i] > P[i + 1]:
    R[i] = 1
  elif P[i - 1] > P[i] and P[i] < P[i + 1]:
    R[i] = 2

result = 0

# しゃくとり法
for l in range(1, N-1):
  count1 = 0
  count2 = 0
  r = l

  if P[l - 1] >= P[l]:
    continue

  while r < N - 1 and count1 < 2 and count2 < 2:
    if R[r] == 1:
      count1 += 1
    elif R[r] == 2:
      count2 += 1
      
    if count1 == 1 and count2 == 1:
      result += 1
      
    r += 1

print(result)