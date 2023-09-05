S = input()
T = input()

min = 1001

for i in range(len(S) - len(T) + 1):
    s = S[i : len(T) + i]
    count = 0
    for j in range(len(T)):
        if T[j] != s[j]:
            count += 1

    if min > count:
        min = count

print(min)
