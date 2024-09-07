S = input()
T = input()
list_s = []
list_t = []
list_diff = []
list_i = []
X = []

if S == T:
    print(0)
    exit()

for i in range(len(S)):
    ord_s = ord(S[i]) - 96
    ord_t = ord(T[i]) - 96
    diff = 26 * (len(T) - i) + (ord_t - ord_s)

    list_diff.append(diff)
    list_i.append(i)

sorted_pairs = sorted(zip(list_diff, list_i))

for j in range(len(S)):
    idx = sorted_pairs[j][1]

    if S[idx] != T[idx]:
        S = S[0:idx] + T[idx] + S[idx+1:]
        X.append(S)


print(len(X))
for k in range(len(X)):

    print(X[k])