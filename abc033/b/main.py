N = int(input())

max = 0
max_name = 0
sum = 0


for i in range(N):
    n, p = map(str, input().split())
    p = int(p)
    sum += p

    if p > max:
        max = p
        max_name = n

if max > sum / 2:
    print(max_name)
else:
    print("atcoder")
