s = input()

chars = []

for c in s:
    chars.append(c)

chars.sort()

if chars[0] == chars[2]:
    print("No")
elif chars[0] == chars[1] and chars[2] == chars[3]:
    print("Yes")
else:
    print("No")
