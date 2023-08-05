a = int(input())
b = int(input())
n = int(input())

for i in range(0, 20001):
    if (n + i) % a == 0 and (n + i) % b == 0:
        print(n + i)
        break
