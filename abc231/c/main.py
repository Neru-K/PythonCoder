import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(Q):
    x = int(input())

    pos = bisect.bisect_left(A, x)

    print(N - pos)