n = int(input())
s = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

newstring = ""

for c in s:
    for i, c2 in enumerate(alphabet):
        if c == c2:
            newstring += alphabet[i + n]
            break

print(newstring)
