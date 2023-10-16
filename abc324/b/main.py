N = int(input())

result = "Yes"

while N > 0:
    if N % 2 == 0:
        N // 2
    elif N % 3 == 0:
        N // 3
    else:
        result = "No"

print(result)
