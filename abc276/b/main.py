N, M = map(int, input().split())

cities = [set() for _ in range(N)]

for i in range(M):
    A, B = map(int,input().split())
    cities[A - 1].add(B)
    cities[B - 1].add(A)

for i in range(N):
    result = [len(cities[i])]
    sorted_c = sorted(list(cities[i]))
    result += sorted_c
    print(*result)