N = int(input())
L = list(map(int, input().split()))

mx = max(L)
sum = sum(L)

if mx < sum - mx:
    print("Yes")
else:
    print("No")
