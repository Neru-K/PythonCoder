import re

S = input()

acgt = re.findall(r"[ACGT]+", S)

leng = []

for s in acgt:
    leng.append(len(s))

if len(leng) == 0:
    print(0)
else:
    print(max(leng))
