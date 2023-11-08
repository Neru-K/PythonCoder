X = int(input())

count = 0
price = 100

while price < X:
    # 1%増を整数で計算する
    increase = price // 100
    price += increase
    count += 1

print(count)
