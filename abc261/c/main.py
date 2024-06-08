N = int(input())

dict = {}

for i in range(N):
    S = input()

    if S in dict:
        dict[S] += 1
        print(S + "(" + str(dict[S]) + ")")
    else:
        dict[S] = 0
        print(S)