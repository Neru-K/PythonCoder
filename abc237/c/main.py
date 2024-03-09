S = input()

lstripped = S.lstrip("a")
rstripped = S.rstrip("a")
stripped = S.strip("a")

if S == S[::-1]:
    print("Yes")
elif len(lstripped) < len(rstripped):
    print("No")
elif stripped == stripped[::-1]:
    print("Yes")
else:
    print("No")