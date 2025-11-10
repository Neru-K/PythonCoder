from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dict = defaultdict(int)

for i in range(N):
    dict[A[i]] += 1

ans = 0

for cnt in dict.values():
    AA = cnt * (cnt - 1) // 2
    B = N - cnt

    ans += AA * B

print(ans)
"""
ヒント 1重ループだけしか回せない。
AAB となると考えると、Aを固定したらBとなるものがいくつあるかは計算できる
"""
