N = int(input())

result = "No"

for i in range(1, 10):
    flag = False
    for j in range(1, 10):
        if i * j == N:
            result = "Yes"
            flag = True
            break

    if flag:
        break

print(result)
