s = input()

result = "Good"

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        result = "Bad"
        break

print(result)
