N, S, M, L = map(int, input().split())

max_6_pack = (N + 5) // 6
max_8_pack = (N + 7) // 8
max_12_pack = (N + 11) // 12

min_cost = float("inf")

for i in range(max_6_pack + 1):
    for j in range(max_8_pack + 1):
        for k in range(max_12_pack + 1):
            if i * 6 + j * 8 + k * 12 >= N:
                cost = i * S + j * M + k * L
                min_cost = min(min_cost, cost)

print(min_cost)
