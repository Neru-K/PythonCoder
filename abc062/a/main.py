x, y = map(int, input().split())

groups = [[1, 3, 5, 7, 8, 10, 12], [4, 6, 9], [2]]

result = "No"

for i in range(3):
    count = 0
    for n in groups[i]:
        if x == n:
            count += 1
        if y == n:
            count += 1

    if count == 2:
        result = "Yes"
        break

print(result)
