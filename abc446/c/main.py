from collections import deque

# 　キューを使うとわかりやすい。
# 　問題文そのままをまず実装してみる
T = int(input())


for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    queue = deque()

    for i in range(N):
        for _ in range(A[i]):
            queue.append(i)

        for _ in range(B[i]):
            queue.popleft()

        while queue and queue[0] <= i - D:
            queue.popleft()

    print(len(queue))
