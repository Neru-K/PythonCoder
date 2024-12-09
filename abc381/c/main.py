N = int(input())
S = input()
S = "$" + S + "$"

max_count = 1

for i in range(N + 2):
    if S[i] == "/":
        count = 0
        j = 1
        while S[i - j] == "1" and S[i + j] == "2":
            count += 1
            j += 1

        max_count = max(max_count, count * 2 + 1)

print(max_count)
