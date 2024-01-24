N = int(input())

X, Y = 0, 0

for i in range(N):
    xi, yi = map(int, input().split())

    X += xi
    Y += yi

if X > Y:
    print("Takahashi")
elif Y > X:
    print("Aoki")
else:
    print("Draw")
