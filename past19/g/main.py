N = int(input())

A = []
zeroidx = []
count = 0

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
    if len(zeroidx) == 0:
        for j in range(N):
            if a[j] == 0:
                zeroidx = [i,j]

def checkResult(r, c, n, t):
    result = False

    if A[A[r][c]-1][n] == A[r][A[c][n]-1]:
        result = True

    return result

for t in range(1, N + 1):
    A[zeroidx[0]][zeroidx[1]] = t
    isExist = True
    for n in range(N):
        for i in range(N):
            for j in range(N):
                isExist = checkResult(i, j, n, t)
                if not isExist:
                    break

            if not isExist:
                break

        if not isExist:
            break

    if isExist:
        count += 1


print(count)

""" N = int(input())

A = []
zeroidx = []
count = 0

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
    if len(zeroidx) == 0:
        for j in range(N):
            if a[j] == 0:
                zeroidx = [i,j]

def checkResult(r, c, n):
    result = False

    if A[A[r][c]-1][n] == A[r][A[c][n]-1]:
        result = True

    return result


for n in range(N):
    A[zeroidx[0]][zeroidx[1]] = n + 1
    isExist = True
    for i in range(N):
        for j in range(N):
            isExist = checkResult(i, j, n)
            if not isExist:
                break

        if not isExist:
            break

if isExist:
    count += 1


print(count) """