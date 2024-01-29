X, A, B, C = map(int, input().split())

usagi = X // A + C
kame = X // B

if usagi < kame:
    print("Hare")
elif usagi > kame:
    print("Tortoise")
else:
    print("Tie")