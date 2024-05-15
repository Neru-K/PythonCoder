S = [input() for _ in range(10)]

rowstart = -1
rowend = -1
colstart = -1
colend = -1

for i in range(10):
    for j in range(10):
        if rowstart == -1 and S[i][j] == "#":
            rowstart = i

        if colstart == -1 and S[i][j] == "#":
            colstart = j

        if rowstart != -1 and rowend == -1:
            if S[i][j] == "#":
                if i == 9:
                    rowend = 9
                elif S[i + 1][j] != "#":
                    rowend = i

        if colstart != -1 and colend == -1:
            if S[i][j] == "#":
                if j == 9:
                    colend = 9
                elif S[i][j + 1] != "#":
                    colend = j

print(str(rowstart + 1)+" "+str(rowend + 1))
print(str(colstart + 1)+" "+str(colend + 1))