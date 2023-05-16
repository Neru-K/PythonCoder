x = list(map(int, input().split()))

x.sort()

count = x.count(x[0])
count2 = x.count(x[4])

if count + count2 == 5 and (count - count2) * (count - count2) == 1:
    print("Yes")
else:
    print("No")
