N = int(input())
A = list(map(int, input().split()))

max_num = 1
ans = 0
sums = []

for i in range(N):
  sums.append(i + A[i])
  
for j in range(N):
  if j + 1 <= max_num:
    ans += 1
    max_num = max(max_num, sums[j])
  else:
    break
  
print(ans)
  