N = int(input())

array = []

for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if i + j + k <= N:
                s = [str(i), str(j), str(k)]
                array.append(" ".join(s))

print("\n".join(array))
