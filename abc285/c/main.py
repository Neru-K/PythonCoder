S = input()

alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

num = 0

for i in range(len(S)):
    for j in range(26):
        if S[i] == alphabet[j]:
            num += (j + 1) * (26 ** (len(S) - 1 - i))
            break

print(num)
