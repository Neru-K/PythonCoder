n = int(input())
s = input()
t = input()

result = "Yes"

for i in range(n):
    if s[i] == t[i]:
        continue
    elif (s[i] == "l" and t[i] == "1") or (s[i] == "1" and t[i] == "l"):
        continue
    elif (s[i] == "o" and t[i] == "0") or (s[i] == "0" and t[i] == "o"):
        continue
    else:
        result = "No"
        break

print(result)
