x, t = map(int, input().split())

diff = x - t

if diff <= 0:
    print(0)
else:
    print(diff)
