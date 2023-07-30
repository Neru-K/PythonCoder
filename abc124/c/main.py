s = input()

zerozero = 0
zeroone = 0
onezero = 0
oneone = 0

for i in range(0, len(s), 2):
    fidx = i
    lidx = i+2

    if s[fidx:lidx] == "00":
        zerozero += 1
    elif s[fidx:lidx] == "01":
        zeroone += 1
    elif s[fidx:lidx] == "10":
        onezero += 1
    elif s[fidx:lidx] == "11":
        oneone += 1
