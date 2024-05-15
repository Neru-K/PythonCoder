S = input()

for i in range(len(S)):
    if i == 3:
        if S[i] != "-":
            print("No")
            exit()

    else:
        if not S[i].isnumeric():
            print("No")
            exit()

print("Yes")