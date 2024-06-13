import copy

N = int(input())
v = list(map(int,input().split()))

v.sort()

while len(v) > 1:
    new = []
    for i in range(0,N,2):
        calc = (v[i] + v[i + 1]) / 2
        new.append(calc)

    v = copy.deepcopy(new)

print(v[0])