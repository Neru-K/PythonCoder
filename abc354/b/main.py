N = int(input())

SC = []
sum = 0

for i in range(N):
    S,C = map(str,input().split())
    SC.append(S)
    sum += int(C)
r = sum % N



SC.sort()
print(SC[r]) 

