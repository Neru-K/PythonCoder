from collections import defaultdict

d = defaultdict(int)

Q = int(input())

id = 0

for i in range(Q):
    q = input()

    if q in d:
        print(d[q])
    else:
        id += 1
        d[q] = id
        print(id)
