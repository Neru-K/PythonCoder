N = int(input())

array = []

for i in range(N):
    s = input().split(" ")
    t = tuple(map(int, s))
    array.append(t)

unique = set(array)
print(len(unique))
