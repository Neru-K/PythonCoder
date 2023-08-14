X = int(input())

if X == 1:
    print(1)
else:
    max = 0
    for i in range(1, 100):
        for j in range(2, 10):
            if i**j > X:
                break
            elif max < i**j:
                max = i**j

    print(max)
