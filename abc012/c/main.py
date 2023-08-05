n = int(input())

diff = 2025 - n

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == diff:
            print(str(i) + " x " + str(j))
