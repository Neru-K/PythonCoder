S = input()
T = input()

pos1 = ord(S[0]) - ord("a")
pos2 = ord(T[0]) - ord("a")

result = "Yes"

distance = pos2 - pos1

for i in range(1, len(S)):
    odr = ord(S[i]) + distance
    if odr > 122:
        odr -= 25
    elif odr < 97:
        odr += 26
    if chr(odr) != T[i]:
        result = "No"
        break

print(result)
