N = int(input())

P = [int(input()) for _ in range(N)]

unique = list(set(P))
unique.sort()

print(unique[len(unique) - 2])
