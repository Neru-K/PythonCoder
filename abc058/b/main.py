O = input()
E = input()
result = ""

for i in range(len(O)):
    result += O[i]
    if i < len(E):
        result += E[i]

print(result)
