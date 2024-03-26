N,K = map(int,input().split())
A = list(map(int,input().split()))

sum = 0

if K % 2 == 0:
    sum = (K + 1) * (K // 2)
else:
    sum = ((K + 1) * (K // 2)) + ((K + 1) // 2)

seta = set()

for a in A:
    if a <= K:
        seta.add(a)

for n in seta:
    sum -= n

print(sum)