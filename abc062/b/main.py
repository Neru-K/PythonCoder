h, w = map(int, input().split())

a = [input().split() for _ in range(h)]

for i in range(h + 2):
    if i == 0 or i == h + 1:
        s = ["#" for _ in range(w + 2)]
        print("".join(s))
    else:
        print("#" + a[i-1][0] + "#")
