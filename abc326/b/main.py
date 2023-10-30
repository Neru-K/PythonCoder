N = input()

flag = False

for n in range(int(N[0]), 10):
    for i in range(0, 10 - int(N[1])):
        for j in range(0, 10):
            if int(str(n) + str(i) + str(j)) < int(N):
                continue

            num = int(n) * i == j

            if num:
                print(str(n) + str(i) + str(j))
                flag = True
                break

        if flag:
            break
    if flag:
        break
