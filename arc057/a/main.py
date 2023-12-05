A, K = map(int, input().split())

t = A
count = 0

if K == 0:
    print(2 * 10**12 - A)

else:
    while A < 2 * 10**12:
        A += 1 + K * t
        t = A
        count += 1

    print(count)
