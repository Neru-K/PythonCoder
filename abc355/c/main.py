N, T = map(int, input().split())
A = list(map(int, input().split()))


def binary_search(numbers, value):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid][0] == value:
            return mid
        elif numbers[mid][0] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


AT = []

for i in range(T):
    AT.append([A[i], i])

AT.sort(key=lambda x: x[0], reverse=False)

#print(AT)

result = []

# 列方向

for i in range(N):
    mx = -1
    flag = True
    for j in range(N):
        target_num = (i + 1) + (N * j)
        searched = binary_search(AT, target_num)

        if searched == -1:
            flag = False
            break

        if AT[searched][1] > mx:
            mx = AT[searched][1]

    if flag:
        result.append(mx)

#print(result)

# 行方向

for i in range(N):
    mx = -1
    flag = True
    base = 1 + (i * N)
    for j in range(N):
        target_num = base + j
        searched = binary_search(AT, target_num)

        if searched == -1:
            flag = False
            break

        if AT[searched][1] > mx:
            mx = AT[searched][1]

    if flag:
        result.append(mx)

#print(result)

#　斜め方向1
def naname1():
    mx = -1
    flag = True
    for i in range(N):
        target_num = 1 + (i * (N + 1))
        searched = binary_search(AT, target_num)

        if searched == -1:
            flag = False
            break

        if AT[searched][1] > mx:
            mx = AT[searched][1]

    if flag:
        result.append(mx)

naname1()

#　斜め方向2
def naname2():
    mx = -1
    flag = True
    for i in range(N):
        target_num = N + (i * (N - 1))
        searched = binary_search(AT, target_num)

        if searched == -1:
            flag = False
            break

        if AT[searched][1] > mx:
            mx = AT[searched][1]

    if flag:
        result.append(mx)

naname2()

result.sort()

if len(result) == 0:
    print(-1)
else:
    print(result[0] + 1)