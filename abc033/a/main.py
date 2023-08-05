n = input()

result = "SAME"

for i in range(3):
    if n[i] != n[i + 1]:
        result = "DIFFERENT"

print(result)
