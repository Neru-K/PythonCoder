M = int(input())
S1 = input()
S1 = S1 + S1 + S1
S2 = input()
S2 = S2 + S2 + S2
S3 = input()
S3 = S3 + S3 + S3

numbers = [0] * 10
arr = [S1, S2, S3]

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and i != k and j != k:
                for l in range(M * 3):
                    numbers[int(arr[i][l])] += 1

                    if numbers in 0:
                        count = i
