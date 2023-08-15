a, b, c, d, e, f, x = map(int, input().split())  # 速さ、距離、休み

tdiv = x // (a + c)
trem = x % (a + c)

if trem > a:
    trem = a

td = (tdiv * a + trem) * b


adiv = x // (d + f)
arem = x % (d + f)

if arem > d:
    arem = d

ad = (adiv * d + arem) * e

if td > ad:
    print("Takahashi")
elif ad > td:
    print("Aoki")
else:
    print("Draw")
