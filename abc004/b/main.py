c = [input() for _ in range(4)]

for i in range(3, -1, -1):
    str = ""
    for j in range(6, -1, -1):
        str += c[i][j]

    print(str)
