L = int(input())

min = 0

for i in range(L-2):
    for j in range(L):
        vol = i * (L - i) * L