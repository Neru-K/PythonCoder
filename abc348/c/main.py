N = int(input())

dict = {}

for i in range(N):
    A, C = map(int,input().split())

    if C in dict:
        if dict[C] > A:
            dict[C] = A
    else:
        dict[C] = A

mx = -1

for c in dict:
    if dict[c] > mx:
        mx = dict[c]

print(mx)