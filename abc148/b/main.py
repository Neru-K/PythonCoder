N = int(input())

s1, s2 = map(str, input().split())

result = ""

for i in range(N):
    result += s1[i] + s2[i]

print(result)
