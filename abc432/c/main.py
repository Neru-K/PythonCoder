import math

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# 最小公倍数を求める
least_num = math.lcm(X, Y)

# 大を小に交換したらいくつ増えるか
diff_num = least_num // X - least_num // Y

if A[0] * Y < A[N - 1] * X:
    print(-1)
    exit()

for i in range(N - 1):
    if (A[i + 1] - A[i]) % diff_num > 0:
        print(-1)
        exit()


num_small = least_num // X # 小の個数
num_large = least_num // Y # 大の個数
diff_change = num_small - num_large # 一回の交換の差

ans = A[0]

for j in range(1,N):
  diff_A = A[j] - A[0] # 個数の差
  times_exchange = diff_A // diff_change # 交換回数
  ans += A[0] - (num_large * times_exchange)
  
print(ans)