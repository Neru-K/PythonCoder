N = int(input())

S = input()

splitted = S.split('"')

for i in range(0, len(splitted), 2):
    sign = ""
    if len(splitted) == 1:
        splitted[i] = splitted[i].replace(",", ".")
    elif i == 0:
        splitted[i] = splitted[i].replace(",", ".") + '"'
    elif i >= len(splitted) - 1:
        splitted[i] = '"' + splitted[i].replace(",", ".")
    else:
        splitted[i] = '"' + splitted[i].replace(",", ".") + '"'

print("".join(splitted))
