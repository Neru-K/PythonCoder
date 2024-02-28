N = int(input())
S = input()
Q = int(input())

alphabet = [[] for _ in range(26)]
s_array = []

for i in range(N):
    s_array.append(S[i])
    alphabet[ord(S[i]) - 97].append(i)

for i in range(Q):
    c, d = map(str, input().split())
    array = alphabet[ord(c) - 97]
    for j in range(len(array)):
        s_array[array[j]] = d
        alphabet[ord(d) - 97].append(array[j])

print("".join(s_array))