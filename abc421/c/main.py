N = int(input())
S = list(input())

ans = 0
tmp = 0
right = 0

for left in range(N):
    if right == left:
        right += 1

    while right < N and S[left] != S[right + 1]:
        tmp += S[right]
        right += 1
    ans += right - left


print(ans, count)
