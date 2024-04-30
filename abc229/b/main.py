A, B = map(str, input().split())

digit = max(len(A), len(B))
zeros = '0' * digit
A = (zeros + A)[-digit:]
B = (zeros + B)[-digit:]

for i in range(digit):
    if int(A[i]) + int(B[i]) > 9:
        print("Hard")
        exit()

print("Easy")