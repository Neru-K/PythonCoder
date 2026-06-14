N = int(input())

given_from = [[] for _ in range(N)]

for i in range(N):
    K, *A = map(int, input().split())

    for a in A:
        given_from[a - 1].append(i + 1)

for l in given_from:
    print(len(l), *l)
