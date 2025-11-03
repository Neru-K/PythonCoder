Q = int(input())

list_br = []
countL = 0
countR = 0
len_yes = 0
is_bad = False

for i in range(Q):
    q, *c = map(str, input().split())

    if q == "1":
        if c[0] == "(":
            countL += 1
        else:
            countR += 1
        list_br.append(c[0])
    else:
        char = list_br.pop()
        if char == "(":
            countL -= 1
        else:
            countR -= 1

        if len(list_br) == len_yes:
            is_bad = False

    if countR > countL:
        is_bad = True
        len_yes = len(list_br) - 1

    if countL == countR and not is_bad:
        print("Yes")
    else:
        print("No")


# 条件1　LとRの数が同じ
# 条件2　1度L<Rになってしまったら以降は悪い括弧列になる

# 条件1を記録するには・・・countL, countRがあれば良い
# 条件2を記録するには・・・フラグがあれば良い
# では他に考えないといけないことは？
# どのタイミングで悪い括弧列になってしまったか。→インデックスを持てば良い。
