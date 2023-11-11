N, Q = map(int, input().split())
S = input()

array = [0] * N
count = 0

for i in range(N - 1):
    if S[i] == S[i + 1]:
        count += 1

    array[i + 1] = count

for j in range(Q):
    l, r = map(int, input().split())
    print(array[r - 1] - array[l - 1])
