from itertools import product

points = list(map(int, input().split()))
S = "ABCDE"

n=5
array = []

count = 0

for pro in product((1, 0), repeat=n):
    count += 1
    if count == 32:
        break

    point = 0
    name = ""

    for i in range(5):
        if pro[i] == 1:
            point += points[i]
            name += S[i]

    array.append([point, name])


array.sort(key=lambda x: x[0], reverse=True)

for j in range(31):
    print(array[j][1])
