S = input()

news = S.lower()

C = S[0].upper()

if S == C+news[1::]:
    print("Yes")
else:
    print("No")