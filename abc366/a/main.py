N, T, A = map(int, input().split())

if T == A:
    print("No")
elif T > (N // 2) or A > (N // 2):
    print("Yes")
else:
    print("No")