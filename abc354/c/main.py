N = int(input())
ACN = []

for i in range(N):
    A,C = map(int,input().split())


    ACN.append([A,C,i+1])




sorted_lst = sorted(ACN, key=lambda x: x[0], reverse=True)
min_c = sorted_lst[0][1]
result = [sorted_lst[0][2]]

for i in range(1, N):
    if sorted_lst[i][1] < min_c:
        min_c = sorted_lst[i][1]
        result.append(sorted_lst[i][2])

result.sort()
    
print(len(result))
print(*result)  # 出力: [[3, 2], [2, 4], [1, 5]]
