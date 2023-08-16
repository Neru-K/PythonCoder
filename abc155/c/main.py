N = int(input())

S = [input() for _ in range(N)]

dict = {}
result = []
max = 1

for i in range(N):
    if S[i] not in dict:
        dict[S[i]] = 1
    else:
        dict[S[i]] += 1
        if dict[S[i]] > max:
            max = dict[S[i]]

for key, v in dict.items():
    if int(v) == max:
        result.append(key)

result.sort()

print("\n".join(result))
