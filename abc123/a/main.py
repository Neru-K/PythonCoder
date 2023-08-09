array = []

for _ in range(5):
    array.append(int(input()))

k = int(input())

result = "Yay!"

for i in range(5):
    for j in range(i+1, 5):
        if array[j] - array[i] > k:
            result = ":("
            break

print(result)
