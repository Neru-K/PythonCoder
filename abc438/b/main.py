N, M = map(int, input().split())

S = list(input())
T = list(input())
ans = []


def f(s_chars):  # Sの1部分を渡した時に、操作回数を返す

    count = 0
    for i in range(len(s_chars)):
        si = int(s_chars[i])
        ti = int(T[i])
        if si < ti:
            count += si + 10 - ti
        else:
            count += si - ti

    return count


for i in range(N - M + 1):
    count = f(S[i : len(T) + i])
    ans.append(count)

ans.sort()

print(ans[0])
