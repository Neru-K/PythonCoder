s = [input() for _ in range(12)]

count = 0

for c in s:
    if c.find("r") > -1:
        count += 1

print(count)
