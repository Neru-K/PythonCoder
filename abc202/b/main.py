S = input()
list = list(S)
list.reverse()

T = ""

for i in range(len(S)):
    if list[i] == "6":
        T += "9"
    elif list[i] == "9":
        T += "6"
    else:
        T += list[i]

print(T)