N = int(input())
A = list(map(int,input().split()))
A.sort()

count = 0

for i in range(N):
  for j in range(i + 1, N):
    if A[i] * 2 <= A[j]:
      count += N - i
      break

print(count)


import bisect
a=[1,2,2,2,3]
 
bisect.bisect_left(a,2)
1
bisect.bisect_right(a,2)
4
bisect.bisect(a,2)
4