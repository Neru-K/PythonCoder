N = int(input())

abc = ["a", "b", "c"]


def recursive(n, s):

    if n == 0:
        print(s)
    else:
        for i in range(3):
            chr = abc[i]
            recursive(n - 1, s + chr)


recursive(N, "")
