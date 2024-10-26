N = 8

visited_row = set()
visited_col = set()

for y in range(N):
    S = input()
    for x in range(N):
        if S[x] == "#":
            visited_row.add(y)
            visited_col.add(x)

not_visited = []

for i in range(N):
    for j in range(N):
        if i not in visited_row and j not in visited_col:
            not_visited.append((i, j))

print(len(not_visited))