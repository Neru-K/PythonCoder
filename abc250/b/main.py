N, A, B = map(int, input().split())

isWhite = False
reverse = True

for i in range(N * A):
    str = ""
    if i % A == 0:
        if reverse:
            reverse = False
        else:
            reverse = True

    if reverse:
        isWhite = False
    else:
        isWhite = True

    for j in range(0, N * B, B):
        if isWhite:
            str += "." * B
            isWhite = False
        else:
            str += "#" * B
            isWhite = True

    print(str)
