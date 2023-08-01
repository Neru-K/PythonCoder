s = input()
n = int(input())

list = []

for c in s:
    for c2 in s:
        list.append(c+c2)

print(list[n - 1])
