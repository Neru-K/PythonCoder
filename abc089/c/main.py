# まず、MARCHから始まる名前だけ振り分ける。
# それぞれの頭文字で何通りあるかを
# あとから引き算？
N = int(input())
chars = "MARCH"
c = [0] * 5

for _ in range(N):
    S = input()
    first_char = S[0]

    for i in range(5):
        if first_char == chars[i]:
            c[i] += 1
            break

count = 0

for j in range(5):
    for k in range(j + 1, 5):
        for l in range(k + 1, 5):
            count += c[j] * c[k] * c[l]

print(count)
