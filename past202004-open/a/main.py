S, T = map(str, input().split())

st = 0
ed = 0

if S[0] == "B":
    st = int(S[1]) * -1 + 1
else:
    st = int(S[0])

if T[0] == "B":
    ed = int(T[1]) * -1 + 1
else:
    ed = int(T[0])

print(abs(st - ed))