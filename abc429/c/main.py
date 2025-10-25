from collections import defaultdict
import math

N = int(input())
A = list(map(int, input().split()))

all = math.comb(N, 3)

dict = defaultdict(int)

for i in range(N):
    dict[A[i]] += 1

morethan1 = []  # 2つ以上
morethan2 = []  # 3つ以上

for j in dict:
    if dict[j] > 1:
        morethan1.append(dict[j])
    if dict[j] > 2:
        morethan2.append(dict[j])

count_morethan1 = 1
count_morethan2 = 1

for m1 in morethan1:
    count_morethan1 *= m1

for m2 in morethan2:
    count_morethan2 += math.comb(m2, 3)

print(all - count_morethan1 - count_morethan2)

"""
全ての中から3つを選ぶ。
全探索をすればできるが、間に合わない。
組み合わせと順列の違いは、順番があるかないか。
今回は順番はある？ない？
順番があるってどういうこと？
席順が決まっている。
325と352が違うものか。今回は違わないので順列ではない。
逆に、全部バラバラになる数と、全部一致する数を数える。
全部の組み合わせ - 重複している数の掛け合わせ - 3つ以上の数
"""
