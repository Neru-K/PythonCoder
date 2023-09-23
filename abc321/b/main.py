N, X = map(int, input().split())
A = list(map(int, input().split()))
sorted = sorted(A)

first = sorted[0]
end = sorted[len(sorted) - 1]
mid = sum(sorted) - end - first

result = -1

for i in range(101):
    if i <= first:
        if X <= first + mid:
            result = 0
            break
    elif i >= end:
        if X <= mid + end:
            result = end
            break
    else:
        if X <= mid + i:
            result = i
            break

print(result)
