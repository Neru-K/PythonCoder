n = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    if a[i] % 2 == 0:  # 嫌い
        if a[i] % 3 == 0:  # 大好き
            count += 3
        elif a[i] % 3 == 1:  # 好き
            count += 1
        elif a[i] % 3 == 2:  # 嫌い
            count += 1

    elif a[i] % 2 == 1:  # 好き
        if a[i] % 3 == 0:
            count += 0

        elif a[i] % 3 == 1:
            count += 0

        elif a[i] % 3 == 2:
            count += 2

print(count)
