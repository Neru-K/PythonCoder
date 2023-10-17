A, B, C = map(int, input().split())

if C % 2 == 0:
    if A**2 > B**2:
        print(">")
    elif A**2 < B**2:
        print("<")
    else:
        print("=")

else:
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")
