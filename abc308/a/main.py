S = list(map(int, input().split()))

isMonoInc = True
isInRange = True
isMultiple25 = True

for i in range(8):
    if i > 0:
        if S[i - 1] > S[i]:
            isMonoInc = False
            break
    if S[i] < 100 or S[i] > 675:
        isInRange = False
        break
    if S[i] % 25 != 0:
        isMultiple25 = False
        break

if isMonoInc and isInRange and isMultiple25:
    print("Yes")
else:
    print("No")
