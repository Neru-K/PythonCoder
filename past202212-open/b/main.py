A, B, C, D = map(int, input().split())

if A / B < C / D:
    print("<")
elif A / B > C / D:
    print(">")
else:
    print("=")