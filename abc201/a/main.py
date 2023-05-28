a = list(map(int, input().split()))

a.sort()
diff = a[1] - a[0]

if a[1] + diff == a[2]:
    print("Yes")
elif a[0] == a[1] == a[2]:
    print("Yes")
else:
    print("No")
