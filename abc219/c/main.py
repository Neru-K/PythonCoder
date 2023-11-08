X = input()
N = int(input())

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
dict = {}

for i, c in enumerate(X):
    dict[c] = i

for i in range(N):
    S = input()
    result = ""
    for c in S:
        result += alphabet[int(dict[c])]

    print(result)
