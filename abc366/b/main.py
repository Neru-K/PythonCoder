N = int(input())

texts = []
maxline = 0

for i in range(N):
    S  = input()
    if len(S) > maxline:
        maxline = len(S)
    for j in range(max(len(S),maxline)):
        if len(texts) <= j:
            texts.append(S[j])

        else:
            if j > len(S) - 1:
                texts[j] = '*' + texts[j]
            else:
                texts[j] = S[j] + texts[j]

for t in range(len(texts)):
    print(texts[t])