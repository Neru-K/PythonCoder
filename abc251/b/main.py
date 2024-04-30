N,W = map(int,input().split())
A = list(map(int,input().split()))

#bit全探索の基本コード(itertools モジュール)
from itertools import product


for pro in product((0, 1), repeat=N):
    sum_p = sum(pro)
    if sum_p > 0 and sum_p < 4:
        sum_a = 0
        for i in range(N):
            if pro[i] == 1:
                sum_a += A[pro[i]]
