N = input()

digit10 = 0

for i in range(len(N)):
    digit10 += int(N[i])

if int(N) % digit10 == 0:
    print("Yes")
else:
    print("No")