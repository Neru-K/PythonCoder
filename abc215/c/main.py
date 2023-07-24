s, k = map(str, input().split())
k = int(k)

list = []

for i in range(len(s)):
    print(s[i])
    for j in range(len(s)):
        if i != j:
            print(s[j])
    print("\n")
