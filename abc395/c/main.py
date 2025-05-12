N = int(input())

A = list(map(int, input().split()))

dict = {}

min_length = 10**6 + 1

for i, a in enumerate(A):
    if a in dict:
        leng = i - dict[a] + 1
        if leng < min_length:
            min_length = leng

    dict[a] = i

if min_length == 10**6 + 1:
    print(-1)
else:
    print(min_length)
