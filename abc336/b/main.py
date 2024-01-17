N = int(input())

b = str(bin(N))

count = 0

for i in range(1, len(b) + 1):
    if i == 1:
        if b[-1] == "0":
            count += 1
        else:
            break

    elif b[-1 * i : -1 * (i - 1)] == "0":
        count += 1
    else:
        break

print(count)
