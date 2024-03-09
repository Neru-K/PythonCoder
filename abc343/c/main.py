N = input()

max = 1
result = 0

for i in range(1, int(N)):
    if i ** 3 > int(N):
        break

    if i ** 3 > max:
        max = i ** 3

    halfNum = len(max) // 2
    halfStrBefore = max[0:halfNum]
    halfStrAfter = max[halfNum + 1:]

print(max)