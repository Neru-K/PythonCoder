N = int(input())
#S = input() 
#S = float(input())
#list_s = input().split()
#A, B, C = input().split()
#A, B = map(int, input().split())
A = list(map(int, input().split()))
#N, M = map(int, input().split())
#A = [list(map(int, input().split())) for _ in range(N)]

A.reverse()

f = 0
sums = []

for i in range(N - 1):
    sum = A[i] + A[i + 1]
    remainder = sum % 10**8
    sums.append(remainder)
    f += f + remainder

print(f)