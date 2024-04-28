N = int(input())
A = list(map(int, input().split()))

s = []
for a in A:
    s.append(a)
    while len(s) > 1 and s[len(s) - 1] == s[len(s) - 2]:
        new = s.pop()
        s.pop()
        s.append(new + 1)

print(len(s))