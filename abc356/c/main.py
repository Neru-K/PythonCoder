from itertools import product

N, M, K = map(int, input().split())

line = []

for i in range(M):
    line.append(list(input().split()))

ans = 0

for pro in product((0, 1), repeat=N):

    isalltrue = True
    
    for i in range(M):
        n = int(line[i][0])
        R = line[i][-1]
        count = 0

        for j in range(1,n+1):
            if pro[int(line[i][j])-1] == 1:
                count += 1

        if count >= K and R == 'x':
            isalltrue = False
            break
        if count < K and R == 'o':
            isalltrue = False
            break

    if isalltrue:
        ans += 1

print(ans)