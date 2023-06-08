n = int(input())
result = n

if n % 2 == 0:
    print(result)
else:
    result += n
    while result % n != 0:
        result += n
    print(result)
