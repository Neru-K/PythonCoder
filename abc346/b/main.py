W, B = map(int,input().split())
S = "wbwbwwbwbwbw" * 21

for i in range(15):
    wcnt = 0
    bcnt = 0
    for j in range(i, i + 200):
        if S[j] == "w":
            wcnt += 1
        else:
            bcnt += 1

        if wcnt == W and bcnt == B:
            print("Yes")
            exit()

print("No")
