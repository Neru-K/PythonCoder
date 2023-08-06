n, m = map(int, input().split())  # n本、m日
a = list(map(int, input().split()))  # 長さ
b = list(map(int, input().split()))  # x日目

result = "Yes"

for i in range(m):
    try:
        index = a.index(b[i])
        a[index] = 0
    except ValueError:
        result = "No"
        break

print(result)
