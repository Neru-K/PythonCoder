N = int(input())

A = list(map(int, input().split()))

maxes = [A[0], A[1]]
maxes.sort(reverse=True)
maxes.append(0)

for i in range(2, N):
    maxes.append(A[i])
    maxes.sort(reverse=True)
    maxes.pop()

    print(maxes[2])
