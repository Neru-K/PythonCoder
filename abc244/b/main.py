N = int(input())
T = input()

currentDirection = 0
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
currentPosition = [0, 0]

for t in T:
    if t == "R":
        currentDirection += 1
        currentDirection = currentDirection % 4
    else:
        currentPosition[0] += direction[currentDirection][0]
        currentPosition[1] += direction[currentDirection][1]

print(str(currentPosition[0]) + " " + str(currentPosition[1]))
