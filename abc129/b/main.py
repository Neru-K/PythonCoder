N = int(input())
W = list(map(int, input().split()))

sum = sum(W)
min = 10001
S1 = 0

for w in W:
    S1 += w
    S2 = sum - S1
    diff = abs(S1 - S2)
    if diff < min:
        min = diff

print(min)
