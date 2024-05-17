import copy

N, M = map(int, input().split())

a = list(map(int,input().split()))

p = [i for i in range(1,N + 1)]

pcopy = copy.deepcopy(p)

if len(a) == 0:
    print(*p)
    exit()

tmp = [a[0]]

result = []

for i in range(M - 1):
    if a[i] + 1 == a[i + 1]:
        tmp.append(a[i + 1]) 
    else:
        l = p[tmp[0]-1:tmp[len(tmp) - 1] + 1]
        l.reverse()

        for j in range(len(l)):
            pcopy[l[-(j+1)]-1] = l[j]

        tmp = [a[i + 1]]

l = p[tmp[0]-1:tmp[len(tmp) - 1] + 1]
l.reverse()
for j in range(len(l)):
    pcopy[l[-(j+1)]-1] = l[j]

print(*pcopy)