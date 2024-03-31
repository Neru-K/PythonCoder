import sys

N, A, B = map(int, input().split())
D = list(map(int, input().split()))

week = A + B

days = []

for i in range(N):
    days.append(D[i] % week)

days.sort()

for i in range(N):
    days.append(days[i] + week)

for i in range(N):
    l = days[i]
    r = days[i + N - 1]

    if r - l + 1 <= A:
        print("Yes")
        exit()

print("No")
