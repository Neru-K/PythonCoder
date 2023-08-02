a = int(input())
b = int(input())
c = int(input())

arr = [a, b, c]

for n in arr:
    if n == max(arr):
        print(1)
    elif n == min(arr):
        print(3)
    else:
        print(2)
