N = int(input())
D = list(map(int, input().split()))

count = 0

for i in range(1, N + 1):
    for j in range(1, D[i - 1] + 1):
        s = str(i) + str(j)
        if len(set(s)) == 1:
            count += 1

print(count)
