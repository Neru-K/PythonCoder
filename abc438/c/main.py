N = int(input())
A = list(map(int, input().split()))

stk = []

for a in A:
    stk.append(a)

    if len(stk) > 3 and (stk[-1] == stk[-2] == stk[-3] == stk[-4]):
        stk.pop()
        stk.pop()
        stk.pop()
        stk.pop()


print(len(stk))
