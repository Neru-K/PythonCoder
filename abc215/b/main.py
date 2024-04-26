N = int(input())

result = 0

for i in range(N):
    if 2**i <= N:
        result = i
    else:
        break

print(result)