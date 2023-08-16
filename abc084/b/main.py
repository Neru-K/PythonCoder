A, B = map(int, input().split())
S = input()

result = "Yes"

for i in range(A + B + 1):
    if i == A:
        if S[i] != "-":
            result = "No"
            break

    else:
        if not S[i].isdigit():
            result = "No"

print(result)
