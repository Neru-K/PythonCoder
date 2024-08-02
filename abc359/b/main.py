N = int(input())
A = list(map(int, input().split()))

#colors = list(set(A))
count = 0
dict = {}


for i, a in enumerate(A):
    if a in dict:
        if i - dict[a] == 2:
            count += 1

    else:
        dict[a] = i

print(count)