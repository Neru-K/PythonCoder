N = int(input())

S = [input() for _ in range(N)]

dict = {}

for i in range(N):
    if S[i] not in dict:
        dict[S[i]] = 1
    else:
        dict[S[i]] += 1

max = 0
result = ""

for name in dict:
    if dict[name] > max:
        max = dict[name]
        result = name

print(result)
