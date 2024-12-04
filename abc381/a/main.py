N = int(input())
S = input()

splitted = S.split("/")

if S == "/":
    print("Yes")

elif len(splitted) == 2:
    set_1 = set(list(splitted[0]))
    set_2 = set(list(splitted[1]))
    if len(splitted[0]) != len(splitted[1]):
        print("No")
    elif len(set_1) == 1 and "1" in set_1 and len(set_2) == 1 and "2" in set_2:
        print("Yes")
    else:
        print("No")

else:
    print("No")
