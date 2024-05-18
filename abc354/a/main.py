H = int(input())
ph = 0

for i in range(99999999999999):
    ph+= 2 ** i
    if ph > H:
        print(i + 1)
        break