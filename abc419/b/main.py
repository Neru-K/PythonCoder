Q = int(input())

array = []

for i in range(Q):
    qnum, *x = map(int, input().split())

    if qnum == 1:
        array.append(x)
    else:
        array.sort()
        num = array.pop(0)
        print(num[0])
