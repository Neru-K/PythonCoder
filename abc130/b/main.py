N, X = map(int, input().split())
L = list(map(int, input().split()))

D = []
count = 0

for i in range(N + 1):
    if i == 0:
        D.append(0)
    else:
        tmp = D[i - 1] + L[i - 1]
        if tmp <= X:
            D.append(tmp)
        else:
            break

    count += 1

print(count)
