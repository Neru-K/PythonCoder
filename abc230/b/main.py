S = input()
T = ""
for _ in range(10**5):
    T += "oxx"

replaced = T.replace(S, "")

if len(T) == len(replaced):
    print("No")
else:
    print("Yes")
