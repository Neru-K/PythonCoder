N, X, Y, Z = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

list = [A, B, []]

for i in range(N):
    list[2].append(i + 1)

list.sort(key=lambda x: x[0], key=lambda y: y[1])

print(list)
