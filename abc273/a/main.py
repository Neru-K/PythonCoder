N = int(input())


def recursive(k):
    if k > 0:
        return recursive(k - 1) * k
    else:
        return 1


print(recursive(N))
