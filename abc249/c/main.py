from itertools import product

N, K = map(int, input().split())

for pro in product((0, 1), repeat=N):
    # proは長さN、各要素が整数 0 か 1 のタプル
    print(pro)
