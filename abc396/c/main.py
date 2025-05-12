# N 黒色ボールの数　価値はB
# M 白色ボールの数　価値はW

N, M = map(int, input().split())

B = list(map(int, input().split()))
B.sort(reverse=True)
W = list(map(int, input().split()))
W.sort(reverse=True)

max = 0

for i in range(N):
  if i > M - 1:
    if B[i] > 0:
      max += B[i]
      
  else:
    if B[i] >= 0 and W[i] >= 0:
      max += B[i]
      max += W[i]
    elif B[i] >= 0 and W[i] < 0:
      max += B[i]
    elif B[i] < 0 and W[i] >= 0:
        if B[i] + W[i] > 0:
          max += B[i]
          max += W[i]
    else:
      break
    
print(max)