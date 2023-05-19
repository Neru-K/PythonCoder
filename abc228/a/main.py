s, t, x = map(int, input().split())

result = "No"

if t > s:
    if x >= s and x < t:
        result = "Yes"

elif t < s:
    if (x >= 0 and x < t) or (x >= s and x < 24):
        result = "Yes"

print(result)
