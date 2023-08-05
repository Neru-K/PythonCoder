list = list(map(int, input().split()))

list.sort()

if list[0] == list[1] == 5 and list[2] == 7:
    print("YES")
else:
    print("NO")
