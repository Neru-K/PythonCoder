N = int(input())
S = input()

count = 0
color = ""

for c in S:
    if c != color:
        count += 1
        color = c

print(count)
