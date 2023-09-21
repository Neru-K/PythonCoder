N = int(input())

lukas = [2, 1]

for i in range(2, N + 1):
    lukas.append(lukas[i - 2] + lukas[i - 1])

print(lukas[len(lukas) - 1])
