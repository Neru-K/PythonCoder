n = int(input())
a = list(map(int, input().split()))
cut = [0]
sum = 0

for i in range(n):
    sum += a[i]
    cut.append(sum % 360)

cut.sort()

piece = []

for j in range(0, len(cut)-1):
    piece.append(cut[j + 1] - cut[j])

piece.append(360 - max(cut))

print(max(piece))
