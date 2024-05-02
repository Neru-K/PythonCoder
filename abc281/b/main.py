S = input()
firstchar = S[0:1]
midchar = S[1:-1]
lastchar = S[-1:]

if not (firstchar.isalpha() and firstchar.isupper()):
    print("No")
    exit()
elif not (lastchar.isalpha() and lastchar.isupper()):
    print("No")
    exit()
elif len(midchar) != 6:
    print("No")
    exit()
elif not midchar.isnumeric():
    print("No")
    exit()
elif 100000 > int(midchar) or int(midchar) > 999999:
    print("No")
    exit()

print("Yes")