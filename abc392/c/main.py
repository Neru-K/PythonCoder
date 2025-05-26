N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

result = []

dict = {}
  
for j in range(N):
  dict[j + 1]= Q[j]
  

  
sorted_pairs = sorted(zip(Q, P))

for k in range(N):
  result.append(dict[sorted_pairs[k][1]])


print(*result, sep=" ")