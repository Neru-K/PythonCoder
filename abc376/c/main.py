N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

x = -1

for i in range(N):
    if i == N-1:
        x = A[i]
        break

    if A[i] > B[i]:
        x = A[i]
        break

if x > -1:
    B.append(x)
    B.sort(reverse=True)

    count = 0

    for j in range(N):
        if A[j] > B[j]:
            count += 1

        if count > 0:
            x = -1
            break


print(x)