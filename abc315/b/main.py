M = int(input())
D = list(map(int, input().split()))

mid = (sum(D) + 1) // 2

for i in range(M):
    if mid <= D[i]:
        print(str(i + 1) + " " + str(mid))
        break
    else:
        mid -= D[i]
