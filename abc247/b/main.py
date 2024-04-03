N = int(input())
st = []

names = []

for i in range(N):
    s,t = map(str,input().split())
    names.append(s)
    if t != s:
        names.append(t)
    
    st.append((s,t))

for i in range(N):
    if names.count(st[i][0]) > 1 and names.count(st[i][1]) > 1:
        print("No")
        exit()

print("Yes")
