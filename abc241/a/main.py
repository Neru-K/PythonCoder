a = list(map(int, input().split()))

index = 0

for i in range(2):
    index = a[index]
    if i == 1:
        print(a[index])
