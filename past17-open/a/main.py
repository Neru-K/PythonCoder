H, W = map(int,input().split())
bmi = W / ((H / 100) ** 2)

if bmi < 20:
    print("A")
elif bmi < 25:
    print("B")
else:
    print("C")