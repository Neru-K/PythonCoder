N, T = map(int, input().split())

AB = []

array = [0,1001,-1]

for i in range(N):
    A, B = map(int, input().split())
    AB.append([A,B])
    if A > array[0]:
        array = [A, B, i]
    elif A == array[0]:
        if B < array[1]:
            array = [A, B, i]

for j in range(N):
    G = T * (array[0] - AB[j][0]) + (AB[j][1] - array[1])
    print(G)
