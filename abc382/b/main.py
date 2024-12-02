N, D = map(int, input().split())
S = input()

list_S = list(S)
list_S.reverse()

ans = []

for i in range(N):
    if D > 0:
        ans.append('.')
    else:
        ans.append(list_S[i])
    if list_S[i] == '@':
        D -= 1

ans.reverse()

print(''.join(ans))