N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    for xnum in range(A[i]):
        ynum = A[i] - xnum

# 答えが存在しないパターンの判定だけでも、まずは考えられると良い
