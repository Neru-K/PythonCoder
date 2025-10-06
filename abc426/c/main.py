N, Q = map(int, input().split())

array = [1] * N
prev_x = 0

for i in range(Q):
    X, Y = map(int, input().split())
    count = 0
    for j in range(prev_x, X):
        count += array[j]
        array[j] = 0

    print(count)
    array[Y - 1] += count
    if X > prev_x:
        prev_x = X
