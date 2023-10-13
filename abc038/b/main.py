H, W = map(int, input().split())
H2, W2 = map(int, input().split())

result = "NO"

if H == H2 or H == W2:
    result = "YES"
elif W == H2 or W == W2:
    result = "YES"

print(result)
