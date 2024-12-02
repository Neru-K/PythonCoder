# まず、MARCHから始まる名前だけ振り分ける。
# それぞれの頭文字で何通りあるかを
# あとから引き算？
N = int(input())

dict = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}

for i in range(N):
    S = input()
    first_char = S[0]

    if first_char in dict:
        dict[first_char] += 1

for c in dict:
    print(dict[c])
