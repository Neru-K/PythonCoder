from math import sqrt

n = int(input())
ans = n
for w in range(1, int(sqrt(n)) + 2):
    h = n // w
    ans = min(ans, abs(w - h) + n - w * h)
print(ans)
