N = int(input())
S = input()

sets = set(list(S))

if len(sets) == 1:
    print("Yes")
else:
    print("No")