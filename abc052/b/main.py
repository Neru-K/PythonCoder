n = int(input())
s = input()

x = 0
max = x

for c in s:
    if c == 'I':
        x += 1
    else:
        x -= 1

    if x > max:
        max = x

print(max)
