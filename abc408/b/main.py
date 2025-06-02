N = int(input())
A = list(map(int, input().split()))

unique_a = list(set(A))
unique_a.sort()

print(len(unique_a))

print(*unique_a, sep=" ")
