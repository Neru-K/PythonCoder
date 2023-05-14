s = input()

s += s
num = 0

for i in range(3):
    num += int(s[i] + s[i + 1] + s[i + 2])

print(num)
