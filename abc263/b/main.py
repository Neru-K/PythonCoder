N = int(input())
P = list(map(int, input().split()))

gen = N - 1
result = 0


while gen > 0:
    gen = P[gen - 1] - 1
    result += 1

print(result)
