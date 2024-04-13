A = list(map(int,input().split()))

sum = 0

for i in range(len(A)):
    if A[i] == 1:
        sum += 2 ** i

print(sum)