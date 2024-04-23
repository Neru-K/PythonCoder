X = list(input())

count = 0

for i in range(3):
    if X[i] == "9":
        if X[i + 1] == "0":
            count += 1
    elif int(X[i]) + 1 == int(X[i + 1]):
        count += 1

if len(set(X)) == 1:
    print("Weak")
elif count == 3:
    print("Weak")
else:
    print("Strong")