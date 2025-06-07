N, L = map(int, input().split())
D = list(map(int, input().split()))

length = L // 3

count_distances = [0] * N
count_distances[0] = 1
ruisekiwa = [0]
distance_from1 = []

for i in range(N - 1):
    distance = (ruisekiwa[i] + D[i]) % L
    ruisekiwa.append(distance)
    count_distances[distance] += 1

""" for r in ruisekiwa:
    distance_from1.append(r % L) """

ruisekiwa.sort()

distances = {}

result = 0

for j in range(length):

    if (
        count_distances[j] > 0
        and count_distances[j + length] > 0
        and count_distances[j + (length * 2)]
    ):
        result += max(
            count_distances[j],
            count_distances[j + length],
            count_distances[j + (length * 2)],
        )

print(result)
