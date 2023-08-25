N = int(input())
array = []

for i in range(N):
    city, score = map(str, input().split())
    array.append([city, score, i + 1])

sorted_data = sorted(array, key=lambda x: (x[0], -int(x[1])))

for j in range(N):
    print(sorted_data[j][2])
