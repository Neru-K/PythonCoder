N = int(input())
a = list(map(int, input()))

array = []

for i in a:
    array.append(a % 2)

print(array)
