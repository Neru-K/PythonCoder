# https://qiita.com/sano192/items/30d394e2c53730dae11f

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
count = 0
lst = [0] * n

for x in c:
    lst[b[x-1]-1] += 1

for i in a:
    count += lst[a[i]]

print(count)
