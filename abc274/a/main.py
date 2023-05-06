A, B = map(int, input().split())
num = round((B/A)*1000) / 1000
str_num = str(num)
if len(str_num) < 5:  # 文字列の長さが5未満の場合
    str_num = str_num + "0" * (5 - len(str_num))  # 末尾に不足分の0を追加する

print(str_num)
