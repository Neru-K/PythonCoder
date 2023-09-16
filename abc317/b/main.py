N = int(input())
A = list(map(int, input().split()))

begin = min(A)
end = max(A)

for i in range(begin, end):
    if i not in A:
        print(i)
