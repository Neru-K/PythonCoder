n = int(input())

s = ""

while n:
    if n % 2 == 1:
        s += "A"
        n -= 1
    else:
        s += "B"
        n //= 2

print(s[::-1])
