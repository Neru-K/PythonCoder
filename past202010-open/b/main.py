x,y = map(int,input().split())

if y == 0:
    print("ERROR")
else:
    ans="{0}.{1:02d}".format((x//y),((x*100//y)%100))
    print(ans)
