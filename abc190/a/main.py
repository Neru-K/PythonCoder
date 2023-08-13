A, B, C = map(int, input().split())

if C:
    if A >= B:
        print("Takahashi")
    else:
        print("Aoki")

else:
    if A > B:
        print("Takahashi")
    else:
        print("Aoki")
