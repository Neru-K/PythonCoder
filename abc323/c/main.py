N, M = map(int, input().split())
A = list(map(int, input().split()))
sorted_A = sorted(A, reverse=True)

obtained_points = []
max = 0
max_index = 0

for i in range(N):
    S = input()
    point = 0
    for j in range(M):
        if S[j] == "o":
            point += A[j]
    if point != 0:
        point += i + 1
    obtained_points.append(point)
    if point > max:
        max = point
        max_index = i

for k in range(N):
    count = 0
    p = obtained_points[k]

    if obtained_points[k] >= max:
        print(0)

    else:
        for l in range(M):
            if p == 0:
                p += k + 1

            count += 1
            p += sorted_A[l]

            if p > max:
                print(count)
                break
