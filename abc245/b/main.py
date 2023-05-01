n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)+1):
    if a.count(i) == 0:
        print(i)
        break
