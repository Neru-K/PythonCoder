N, X = map(int, input().split())
A = list(map(int, input().split()))

knows = [False] * N

i = X
while knows[i - 1] is False:
    knows[i - 1] = True
    i = A[i - 1]

print(knows.count(True))
