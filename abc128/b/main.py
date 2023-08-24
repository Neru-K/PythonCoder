N = int(input())
array = []

for i in range(N):
    city, score = map(str, input().split())
    array.append([city, score, i + 1])

sorted_data = sorted(array, key=lambda x: (x[0], -int(x[1])))

dict = {}

for j in range(N):
    dict[sorted_data[j][2]] = j + 1

for k in range(N):
    print(dict[array[k][2]])
