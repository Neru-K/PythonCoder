S = input()

arr_pos = []
result_s = list(S)

"""
条件分岐

・最初の１文字目の場合
  Aの場合
    lastidxを更新
  それ以外
    特になし

・2文字目以降の場合
  ・Aの場合
    lastidxを更新
    firstidxをリセット

  ・Wの場合
    前の文字がWの場合
      firstidxを更新
    前の文字がAの場合
      firstidxを更新

  ・それ以外
    lastidx, firstidxが-1じゃない場合、配列に追加
    lastidx, firstidxをリセット


"""

firstidx = -1
lastidx = -1
flag = False

for i in range(len(S) - 1, -1, -1):
    if i == len(S) - 1:
        if S[i] == "A":
            lastidx = i

        continue

    if S[i] == "A":
        if lastidx != -1 and firstidx != -1:
            arr_pos.append((firstidx, lastidx))

        lastidx = i
        firstidx = -1

    elif S[i] == "W":
        if S[i + 1] == "A":
            firstidx = i

        elif S[i + 1] == "W":
            firstidx = i

    else:
        if lastidx != -1 and firstidx != -1:
            arr_pos.append((firstidx, lastidx))
            lastidx = -1
            firstidx = -1

    if i == 0 and S[i] == "W" and lastidx != -1 and firstidx != -1:
        arr_pos.append((firstidx, lastidx))
        lastidx = -1
        firstidx = -1

for pair in arr_pos:
    result_s[pair[0]] = "A"
    for l in range(pair[0] + 1, pair[1] + 1):
        result_s[l] = "C"

print(*result_s, sep="")
