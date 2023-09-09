N = int(input())

result = ""

for i in range(N + 1):
    isExist = False
    for j in range(1, 10):
        if i % (N / j) == 0:
            result += str(j)
            isExist = True
            break
    if not isExist:
        result += "-"

print(result)
