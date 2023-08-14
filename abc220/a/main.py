A, B, C = map(int, input().split())

times = int(A / C)

if A % C != 0:
    times = (A // C) + 1

result = -1

if C * times <= B:
    result = C * times

print(result)
