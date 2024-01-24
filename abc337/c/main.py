N = int(input())
A = list(map(int, input().split()))

row = [i + 1 for i in range(N)]

ans = [""] * N

# zipでペアにしてソート
sorted_pairs = sorted(zip(A, row))

next = sorted_pairs[0][1]

for i in range(N):
    ans[i] = str(next)
    if next < N:
        next = sorted_pairs[next][1]

print(" ".join(ans))
