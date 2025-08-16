import collections

N = int(input())
A = list(map(int, input().split()))

dict = collections.defaultdict(int)
ans = 0

# コツ：同じインデックスでまとめる。
# コツ：ペアを探すときは、後ろを固定して前を追加していくみたいなのがありがちなパターン

for j in range(N):
    key = A[j] - j
    ans += dict[key]

    key_i = -A[j] - j
    dict[key_i] += 1


print(ans)
