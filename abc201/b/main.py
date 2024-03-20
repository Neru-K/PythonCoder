N = int(input())
ST = []

for i in range(N):
    S, T = map(str, input().split())
    ST.append([S, int(T)])

sorted_lst = sorted(ST, key=lambda x: x[1], reverse=True)
print(sorted_lst[1][0])
