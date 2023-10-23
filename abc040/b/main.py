import math

n = int(input())

mx = 0

for i in range(1, math.floor(n**0.5)):
    num = n // i
    if n - (num * num) > mx:
        mx = n - (num * num)
