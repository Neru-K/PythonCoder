s, t = map(str, input().split())
a, b = map(int, input().split())
u = input()

if u == s:
    a -= 1
else:
    b -= 1

print(str(a) + " " + str(b))
