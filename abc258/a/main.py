k = int(input())

shou = int(k / 60)
amari = k % 60
hours = 21 + shou
if hours >= 24:
    hours = hours - 24

minutes = amari

hstr = "0" + str(hours)
mstr = "0" + str(minutes)

print(hstr[-2:] + ":" + mstr[-2:])
