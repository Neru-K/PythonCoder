from collections import deque

N, Q = map(int, input().split())

positions = deque([(str(i + 1), "0") for i in range(N)])

for _ in range(Q):
    q1, q2 = input().split()

    if q1 == "1":
        x, y = positions[0]
        if q2 == "U":
            positions.appendleft((x, str(int(y) + 1)))
        elif q2 == "R":
            positions.appendleft((str(int(x) + 1), y))
        elif q2 == "D":
            positions.appendleft((x, str(int(y) - 1)))
        elif q2 == "L":
            positions.appendleft((str(int(x) - 1), y))

        positions.pop()

    elif q1 == "2":
        idx = int(q2) - 1
        print(" ".join(positions[idx]))
