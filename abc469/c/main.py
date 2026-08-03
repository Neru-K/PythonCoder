N = int(input())
S = input()

countx = 0

for i in range(N):
    if S[i] == "x":
        countx += 1
        print(i + 1)

for _ in range(N - countx):
    print(N)
