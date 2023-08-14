H, M = map(str, input().split())

H = "0" + H
H = H[-2:]

M = "0" + M
M = M[-2:]

print(H)
print(M)

if int(H[0] + M[0]) < 24 and int(H[1] + M[1]) < 60:
    print(H + " " + M)
else:
    for i in range(int(H), 24):
        breakFlag = False
        H = "0" + str(i)
        H = H[-2:]
        for j in range(int(M), 60):
            M = "0" + str(j)
            M = M[-2:]

            if int(H[0] + M[0]) < 24 and int(H[1] + M[1]) < 60:
                print(H + " " + M)
                breakFlag = True
                break

        if breakFlag:
            break
