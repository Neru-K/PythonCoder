S = input()

array = []

for i in range(len(S) - 2):
    num = int("".join([S[i], S[i + 1], S[i + 2]]))
    array.append(abs(753 - num))

print(min(array))
