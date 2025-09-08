T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    avg = (A + B + C) // 3
    print(min(avg, A, C))

# 答えの上限、下限を考える。
