N, M  = map(int, input().split())
array = []

for _ in range(N):
  array.append(set())

for _ in range(M):
  A, B = map(int, input().split())
  if B - 1 in array[A - 1] or A - 1 in array[B - 1]:
    print("No")
    exit()
    
  array[A - 1].add(B - 1)
  array[B - 1].add(A - 1)
  
for st in array:
  if len(st) != 2:
    print("No")
    exit()
    
print("Yes")