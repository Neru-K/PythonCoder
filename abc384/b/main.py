N, R = map(int, input().split())

for i in range(N):
    D, A = map(int, input().split())
    if D == 1:
        if R >= 1600 and R <= 2799:
            R += A

    else:
        if R >= 1200 and R <= 2399:
            R += A

    R = min(4229, R)
    R = max(0, R)

print(R)