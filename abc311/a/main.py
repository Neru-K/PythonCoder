n = int(input())
s = input()

a = 0
b = 0
c = 0
count = 1

for char in s:
    if char == "A":
        a += 1
    elif char == "B":
        b += 1
    elif char == "C":
        c += 1

    if a > 0 and b > 0 and c > 0:
        print(count)
        break

    count += 1
