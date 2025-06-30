Q = int(input())

line = []
idx = 0
pos_head = [0]

for _ in range(Q):
    q, *r = list(map(int, input().split()))
    if q == 1:
        line.append(r[0])
        pos_head.append(pos_head[len(pos_head) - 1] + r[0])
    elif q == 2:
        idx += 1
    else:
        k = r[0]
        print(pos_head[k - 1 + idx])
