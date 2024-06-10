import copy

N = int(input())

result = [1]

for i in range(1,N):
    cp = copy.copy(result)
    result.append(i + 1)
    result += cp

print(*result)