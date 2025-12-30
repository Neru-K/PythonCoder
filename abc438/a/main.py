D, F = map(int, input().split())

rem = D % 7
ans = (F - rem) % 7

if ans == 0:
    print(7)
else:
    print(ans)
