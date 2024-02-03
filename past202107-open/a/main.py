S = input()
sumOdd = 0
sumEven = 0

for i in range(len(S) - 1):
    if i % 2 == 0:
        sumOdd += int(S[i])
    else:
        sumEven += int(S[i])

if (sumOdd * 3 + sumEven) % 10 == int(S[14]):
    print("Yes")
else:
    print("No")