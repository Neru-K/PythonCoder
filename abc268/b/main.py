s = input()
t = input()

try:
    index = t.index(s)
    if index == 0:
        print("Yes")
    else:
        print("No")
except ValueError:
    print("No")
