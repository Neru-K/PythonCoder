S = input()
T = input()

idx = 0
result = []

for i in range(len(T)):
    if T[i] == S[idx]:
        result.append(i + 1)
        idx += 1
    
print(*result)