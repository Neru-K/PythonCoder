from itertools import product


N = int(input())
A = list(map(int, input().split()))

ans = 0

for pro in product((0, 1), repeat=N):
    count = 0
    prev = 0.5
    for i in range(N):
        if pro[i] == 0:
            now = prev - A[i]
        else:
            now = prev + A[i]
        if (prev > 0 and now < 0) or (prev < 0 and now > 0):
            count += 1

        prev = now

    if count > ans:
        ans = count

print(ans)
