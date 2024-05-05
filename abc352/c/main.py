N = int(input())
list_a = []
list_b = []
max_diff = -1
idx_diff = -1


for i in range(N):
    A, B = map(int,input().split())
    list_a.append(A)
    list_b.append(B)

    if B - A > max_diff:
        max_diff = B - A
        idx_diff = i

print(sum(list_a) + list_b[idx_diff] - list_a[idx_diff])