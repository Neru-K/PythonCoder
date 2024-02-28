N = int(input())
P = list(map(int,input().split()))
Q = int(input())

array = [0] * N #人1、人2、...

for i in range(N):
    array[P[i] - 1] = i + 1

for i in range(Q):
    A, B = map(int, input().split())
    print(P[min(array[A - 1], array[B - 1]) - 1])
