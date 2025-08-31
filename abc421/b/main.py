X, Y = map(int, input().split())


def f(a1, a2):
    x = a1 + a2
    rev = str(x)[::-1]
    return int(rev)


ans = 0

for i in range(3, 11):
    ans = f(X, Y)
    X = Y
    Y = ans

print(ans)
