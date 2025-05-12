N, M = map(int, input().split())

array = [-1] * M

A = list(map(int, input().split()))

for i, a in enumerate(A):
  if array[a - 1] == -1:
      array[a - 1] = i
      
max_arr = 0
      
for arr in array:
  if arr > max_arr:
    max_arr = arr
    
if -1 in array:
  print(0)
else:
  print(N - max_arr)