N = int(input())
A = list(map(int, input().split()))

array = []

for i in range(N):
    array.append((A[i], i + 1))


sorted_lst = sorted(array, key=lambda x: x[0], reverse=False)

print(sorted_lst[-2][1])

