s = input()

result = "No"

for i in range(2):
    if s[i] != s[i + 1]:
        result = "Yes"
        break

print(result)
