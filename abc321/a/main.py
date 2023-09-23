N = input()

result = "Yes"

for i in range(1, len(N)):
    if int(N[i]) >= int(N[i - 1]):
        result = "No"
        break

print(result)
