import heapq

Q = int(input())

th = []

for i in range(Q):

    q, h = map(int, input().split())

    if q == 1:
        heapq.heappush(th, h)
    elif q == 2:
        while th and th[0] <= h:
            heapq.heappop(th)

    print(len(th))


# クエリの数だけループを回す
# 　各クエリの1 or 2　と、木の高さをとる。
# 　クエリが1だったら、XXX 2だったらYYYみたいな分岐をする。
# 　1だったら：thのリストに木の高さ（h）を記録する　thの役割：現在残っている木の高さを記録する
# 　2だったら：thをループして、現在残っている木を精査する。→　thの中から、hより高い木だけを選ぶ。
##　→　thの中からhより高い木だけを残して、th2に入れる。　th2の役割：クエリ2が出た時点で、thからhより低い木を消した後の木の高さを記録する
# 　thの内容をth2で上書きする。
# thに残っている木の本数をprintする。
# 　heapq 優先度付きキュー
