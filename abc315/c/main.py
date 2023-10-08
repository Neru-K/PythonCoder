N = int(input())

point = [0, 0, 0]
flavor = [0, 0, 0]

for i in range(N):
    F, S = map(int, input().split())
    if S > point[0]:
        point[2] = point[1]
        point[1] = point[0]
        point[0] = S

        flavor[2] = flavor[1]
        flavor[1] = flavor[0]
        flavor[0] = F

    elif S > point[1]:
        point[2] = point[1]
        point[1] = S
        flavor[2] = flavor[1]
        flavor[1] = F

    elif S > point[2]:
        point[2] = S
        flavor[2] = F


highest = point[0]
second, third = 0, 0
if flavor[0] == flavor[1]:
    second = point[1] // 2
else:
    second = point[1]

if flavor[0] == flavor[2]:
    third = point[2] // 2
else:
    third = point[2]

highest2 = 0

if flavor[1] != flavor[2]:
    highest2 = point[1] + point[2]

print(max(highest + max(second, third), highest2))
