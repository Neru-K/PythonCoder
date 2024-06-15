N, A = map(int, input().split())
T = list(map(int, input().split()))

prev = 0

for i in range(N):
    spent = max(prev +  A, T[i] + A)
    prev = spent

    print(spent)