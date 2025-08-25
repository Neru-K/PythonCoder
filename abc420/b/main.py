N, M = map(int, input().split())

s = []
for _ in range(N):
    s.append(input())

ans = [0] * N
points = [0] * N

for j in range(M):
    count0 = []
    count1 = []
    for i in range(N):
        num = s[i][j]
        if num == "0":
            count0.append(i)
        elif num == "1":
            count1.append(i)

    if len(count0) == 0 or (len(count1) < len(count0)):
        for k in range(len(count1)):
            ans[count1[k]] += 1
    elif len(count1) == 0 or (len(count0) < len(count1)):
        for k in range(len(count0)):
            ans[count0[k]] += 1

max_ans = max(ans)
f_ans = []

for l in range(N):
    if ans[l] == max_ans:
        f_ans.append(l + 1)

print(*f_ans, sep=" ")
