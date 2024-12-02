A = list(map(int, input().split()))

count = 0
dict = {1:0,2:0,3:0,4:0}

for i in range(4):

    dict[A[i]] += 1

    if dict[A[i]]==2:
        count += 1
        dict[A[i]] = 0

print(count)