N, M = map(int, input().split())

S = input()

muji = M
logo = 0
min = N

for c in S:
    if c == "0":
        muji = M
        logo = 0

    elif c == "1":
        if muji > 0:
            muji -= 1
        else:
            logo -= 1

    else:
        logo -= 1

    if logo < min:
        min = logo

print(abs(min))
