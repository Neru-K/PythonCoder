N = input()

ans = 0

while len(N) > 1:
    splitted = list(N)
    sumn = 0
    for n in N:
        sumn += int(n) ** 2

    N = str(sumn)

ans = int(N)

if ans == 1:
    print("Yes")
else:
    print("No")
