N, X, Y, Z = map(int,input().split())

mx = max(X,Y)
mn = min(X,Y)

if mn <= Z <= mx:
    print("Yes")
else:
    print("No")