S = input()

count = 0

if "R" in S:
    count += 1

for i in range(2):
    if S[i] == "R" and S[i + 1] == "R":
        count += 1

print(count)
