from itertools import combinations

N,W = map(int,input().split())

mn = min(3, N)
A = ([0] * mn) + list(map(int,input().split()))

comb = combinations(A, mn)

set_n = set()
count = 0

for i in list(comb):
    sm = sum(i)
    if sm not in set_n and 0 < sm and sm <= W:
        set_n.add(sm)
        count += 1
		
print(count)