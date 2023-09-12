H, M = map(int, input().split())

i = H
j = M

breakflg = False

while i < 49:
    if i < H:
        continue

    hour = "0" + str(i % 24)
    hour = str(hour[-2:])

    while j <= 60:
        if i <= H and j < M:
            continue

        minute = "0" + str(j)
        minute = minute[-2:]
        first_num = int(hour[0] + minute[0])
        second_num = int(hour[1] + minute[1])
        if first_num >= 0 and first_num <= 23:
            if second_num >= 0 and second_num <= 59:
                print(str(i % 24) + " " + str(j))
                breakflg = True
                break

        j = j + 1

    j = 0

    if breakflg:
        break

    i = i + 1
