N, L = map(int, input().split())

taste = []
min = 99999

for i in range(N):
    taste.append(L + i)
    if abs(L + i) < min:
        min = abs(L + i)

sum = sum(taste)

if sum >= 0:
    print(sum - min)
else:
    print(sum + min)
