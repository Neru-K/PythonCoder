n = int(input())

p = list(map(int, input().split()))

fst = p[0]
max = 0

for i in range(1, len(p)):
    if p[i] > max:
        max = p[i]

if fst == max:
    print(1)
elif fst < max:
    print(max - fst + 1)
else:
    print(0)
