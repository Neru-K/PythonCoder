n = int(input())
s = input()
result = ""

if s[n - 1] == "o":
    result = "Yes"
elif s[n - 1] == "x":
    result = "No"

print(result)
