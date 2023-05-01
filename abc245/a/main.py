A, B, C, D = map(int, input().split())

takahashi = A * 3600 + B * 60
aoki = C*3600 + D * 60 + 1

if takahashi < aoki:
    print("Takahashi")

elif aoki < takahashi:
    print("Aoki")
