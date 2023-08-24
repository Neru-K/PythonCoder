s = int(input())


def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1


i = 1
a = s
set = {a}

while True:
    i += 1
    a = int(f(a))
    if a in set:
        break
    else:
        set.add(a)

print(i)
