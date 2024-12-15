from collections import deque

N = int(input())

T = []
K = []
A = []

for i in range(N):
    t, k, *a = list(map(int, input().split()))

    T.append(t)
    K.append(k)
    A.append(a)

queue = deque(A[N-1])
done = set()
time = T[N - 1]

while len(queue) > 0:
    p = queue.popleft()

    if p not in done:
        done.add(p)
        time += T[p - 1]
        queue.extend(A[p - 1])


print(time)