S = input()

count_L = 0
count_U = 0
for c in S:
    if c.islower():
        count_L += 1
    else:
        count_U += 1

if count_L > count_U:
    S = S.lower()
else:
    S = S.upper()

print(S)