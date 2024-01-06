A, B, C = map(int, input().split())


def binary_gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b

    # kをaとbの最大の共通の2の累乗とする（aとbがともに偶数である限り2で割り続ける）
    k = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        k += 1

    # aを奇数にする
    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        # bを奇数にする
        while (b & 1) == 0:
            b >>= 1

        # aとbの絶対値の差の一方を新しいbとする
        if a > b:
            a, b = b, a - b
        else:
            b = b - a

    return a << k


S = binary_gcd(A, binary_gcd(B, C))

print(int(A // S - 1) + int(B // S - 1) + int(C // S - 1))
