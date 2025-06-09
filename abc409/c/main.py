N, L = map(int, input().split())
D = list(map(int, input().split()))

if L % 3 != 0:
    print(0)
    exit()

length = L // 3

count_distances = [0] * L
count_distances[0] = 1
ruisekiwa = [0]

for i in range(N - 1):
    distance = (ruisekiwa[i] + D[i]) % L
    ruisekiwa.append(distance)
    count_distances[distance] += 1

result = 0

for j in range(length):

    if (
        count_distances[j] > 0
        and count_distances[j + length] > 0
        and count_distances[j + (length * 2)]
    ):

        result += (
            count_distances[j]
            * count_distances[j + length]
            * count_distances[j + (length * 2)]
        )


print(result)
