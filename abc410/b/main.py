N, Q = map(int, input().split())

X = list(map(int, input().split()))
box = [0] * N

for i in range(Q):
    if X[i] == 0:
        min_kazu = Q + 1
        for j in range(N):
            min_kazu = min(min_kazu, box[j])
        for k in range(N):
            if box[k] == min_kazu:
                X[i] = k + 1
                break

    box[X[i] - 1] += 1

print(*X, sep=" ")
