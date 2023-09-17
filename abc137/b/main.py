K, X = map(int, input().split())

arr = []
num = K - 1
left = X - num
right = X + num

if X + num > 1000000:
    right = 1000000
    left = 1000000 - K

if X - num < -1000000:
    left = -1000000
    right = -1000000 + K

for i in range(left, right + 1):
    arr.append(str(i))

print(" ".join(arr))
