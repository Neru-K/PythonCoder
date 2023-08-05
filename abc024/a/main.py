a, b, c, k = map(int, input().split())

s, t = map(int, input().split())

childs = s * a
adults = t * b

discount = 0

if s + t >= k:
    discount = (s + t) * c

print(childs + adults - discount)
