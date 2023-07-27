n = int(input())
a = list(map(int, input().split()))

index = []
index2 = []
index3 = []

for i in range(1, n+1):

    for j in range(len(a)):

        if a[j] == i:
            if i == 1:
                index.append(j + 1)
            if i == 2:
                index2.append(j + 1)
            if i == 3:
                index3.append(j + 1)

mid = [index[1], index2[1], index3[1]]

mid.sort()

print(str(mid[0]) + " " + str(mid[1]) + " " + str(mid[2]))
