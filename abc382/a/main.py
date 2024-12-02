N, D = map(int, input().split())
S = input()
cnt_cookie = 0

for i in range(N):
    if S[i] == "@":
        cnt_cookie += 1

print(N - cnt_cookie + D)