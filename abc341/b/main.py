N = int(input())
A = list(map(int, input().split()))

S = [list(map(int, input().split())) for _ in range(N - 1)]

array = []

for i in range(N):
    array.append([A[i], i])
    
flag = True
while flag:
    flag = False
    array.sort(reverse=True, key=lambda x:x[0])
    for i in range(N):
        idx = array[i][1]
        quantity = array[i][0]

        if quantity > S[idx][0]:
            array[i][0] -= S[idx][1]
            A[idx] -= S[idx][1]
            flag = True
            break

print(array)

