N = int(input())
H = list(map(int,input().split()))

h = H[0]

for i in range(N - 1):
    if H[i] < H[i + 1]:
        h = H[i + 1]
    else:
        break

print(h)