A, B, C = map(int, input().split())

plus = False
minus = False

if A + B == C:
    plus = True

if A - B == C:
    minus = True

if plus and minus:
    print("?")
elif plus and not minus:
    print("+")
elif not plus and minus:
    print("-")
else:
    print("!")
