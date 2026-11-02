N = int(input())

A = list(map(int, input().split()))

maxes = [A[0], A[1]]
maxes.sort(reverse=True)
maxes.append(0)

for a in A[:3]:
    maxes.append(a)
    maxes.sort(reverse=True)
    maxes.pop()

    print(maxes[2])
