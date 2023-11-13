X = input()

result = "YES"

i = 0

while i < len(X):
    if i != len(X) - 1:
        if X[i] + X[i + 1] == "ch":
            i = i + 2
            continue

    if X[i] != "o" and X[i] != "k" and X[i] != "u":
        result = "NO"
        break

    i = i + 1

print(result)
