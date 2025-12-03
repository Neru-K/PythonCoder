import math

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

least_num = math.lcm(X, Y)
diff_num = least_num // X - least_num // Y

if A[0] * Y < A[N - 1] * X:
    print(-1)
    exit()

ans = 0

for i in range(N - 1):
    if (A[i + 1] - A[i]) % diff_num > 0:
        print(-1)
        exit()


#
