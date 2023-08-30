N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())

LR = [list(map(int, input().split())) for _ in range(Q)]

class1 = [0]
class2 = [0]

for i in range(N):
    if CP[i][0] == 1:
        class1.append(CP[i][1] + class1[i])
        class2.append(class2[i])
    else:
        class1.append(class1[i])
        class2.append(CP[i][1] + class2[i])

for j in range(Q):
    result = []
    result.append(str(class1[LR[j][1]] - class1[LR[j][0] - 1]))
    result.append(str(class2[LR[j][1]] - class2[LR[j][0] - 1]))
    print(" ".join(result))
