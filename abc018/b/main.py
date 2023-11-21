S = input()
N = int(input())

for i in range(N):
    l, r = map(int, input().split())
    S = S[: l - 1] + "".join(list(reversed(S[l - 1 : r]))) + S[r:]
print(S)
