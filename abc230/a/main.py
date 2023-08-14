N = int(input())

if N > 41:
    N += 1
    strN = "00" + str(N)
    print("AGC" + strN[-3:])
else:
    strN = "00" + str(N)
    print("AGC" + strN[-3:])
