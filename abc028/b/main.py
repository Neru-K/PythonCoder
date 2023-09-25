S = input()

count = [0, 0, 0, 0, 0, 0]

for c in S:
    count[ord(c) - 65] += 1

strs = []

for i in count:
    strs.append(str(i))

print(" ".join(strs))
