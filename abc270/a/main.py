a, b = map(int, input().split())
points = [4, 2, 1]
sunuke = []

for i in range(len(points)):
    if a - points[i] >= 0:
        sunuke.append(points[i])
        a = a - points[i]

    if b - points[i] >= 0:
        sunuke.append(points[i])
        b = b - points[i]

unique = list(set(sunuke))

print(sum(unique))
