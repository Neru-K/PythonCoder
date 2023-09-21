A, B = map(int, input().split())

count = 0

for i in range(A, B + 1):
    numstr = str(i)
    if numstr == numstr[::-1]:
        count += 1

print(count)
