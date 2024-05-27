N = int(input())

count = 0

for i in range(N):
    A, B = map(int, input().split())

    r = B - A
    if r >= 500:
        r %= 500

    if r >= 100:
        r %= 100

    if r >= 50:
        count += r // 50
        r %= 50

    if r >= 10:
        r %= 10

    if r >= 5:
        count += r // 5
        r %= 5

    if r >= 1:
        r %= 1

print(count)