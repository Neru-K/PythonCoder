N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]

obj = {}
unique = list(set(s))

for i in range(len(unique)):
    obj[unique[i]] = s.count(unique[i])
    obj[unique[i]] = obj[unique[i]] - t.count(unique[i])

max_key = max(obj, key=obj.get)
max_value = obj[max_key]

print(max(max_value, 0))
