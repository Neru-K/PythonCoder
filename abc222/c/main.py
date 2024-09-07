N, M = map(int, input().split())

def jan(h1, h2):
    if h1 == h2:
        return 1
    else:
        if h1 == 'G' and h2 == 'C' or\
        h1 == 'C' and h2 == 'P' or \
        h1 == 'P' and h2 == 'G':
            return 1
        else:
            return 2

result = []

for i in range():
    result.append(input())

win = [0] * N
lose = [0] * N
        
for c in range(M):
    for r in range(0,N*2,2):
        battle = jan(result[r-1][c], result[r][c])
        if battle == 0:
            win[r//2]