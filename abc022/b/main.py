N = int(input())
A = [int(input()) for _ in range(N)]
unique = set(A)

print(len(A) - len(unique))
