A, B = map(int, input().split())

for i in range(B, 0, -1):
    if (A + i - 1) // i < B // i:
        print(i)
        break
