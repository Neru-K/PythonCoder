N = int(input())

S = list(map(str, input().split()))

num = set(S)

if len(num) == 3:
    print("Three")
else:
    print("Four")
