S = input()

a = ""
result = "No"

for i in range(len(S)):
    concat = a + S
    if concat == concat[::-1]:
        result = "Yes"
        break
    a += "a"

print(result)
