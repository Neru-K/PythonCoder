S = input()
s = sorted(S)
alphabet = [0] * 26

for i in range(len(S)):
    alphabet[ord(s[i]) - 97] += 1

max = 0
result = 0

for i in range(26):
    if alphabet[i] > max:
        max = alphabet[i]
        result = i + 97

print(chr(result))
