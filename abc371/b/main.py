N, M = map(int, input().split())

children = [0] * N

for i in range(M):
    A, B = map(int, input().split())
    if B == "M":
        if children[A - 1] == 0:
            print("Yes")

            children[A - 1] += 1

        else:
            print("No")

    else:
        print("No")