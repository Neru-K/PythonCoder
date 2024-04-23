S = input()
T = input()

diff = (ord(T[0]) - ord(S[0]) + 26) % 26

for i in range(len(S)):
    shifted_char = chr((ord(S[i]) - ord('a') + diff) % 26 + ord('a'))
    if T[i] != shifted_char:
        print("No")
        exit()

print("Yes")
