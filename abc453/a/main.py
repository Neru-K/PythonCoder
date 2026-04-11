N = int(input())
S = list(input())

for i in range(N):
    if S[i] == "o":
        S[i] = ""
    else:
        break

print(*S, sep="")
