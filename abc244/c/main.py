N = int(input())

maxnum = 2 * N + 1

lst = [0] * maxnum

for i in range(maxnum):
    for j in range(maxnum):
        if lst[j] == 0:
            print(j + 1)
            lst[j] = 1
            if j == maxnum - 1:
                print(0)
                exit()
            break


    hisnum = int(input())
    lst[hisnum - 1] = 1