B = int(input())

result = -1

for i in range(1, 20):
    if i**i == B:
        result = i
        break

print(result)
