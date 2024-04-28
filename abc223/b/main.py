S = input()
N = int(len(S))
S += S

set_s = set()

for i in range(N):
    set_s.add(S[i:i+N])

sorted = sorted(list(set_s))

print(sorted[0])
print(sorted[len(sorted) - 1])