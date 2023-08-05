import math

a, b = map(int, input().split())

len = math.sqrt(a * a + b * b)

print(str(a/len) + " " + str(b/len))
