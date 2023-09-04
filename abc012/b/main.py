N = int(input())

hour = N // 3600
min = (N - (hour * 3600)) // 60
sec = N - hour * 3600 - min * 60

hstr = "0" + str(hour)
mstr = "0" + str(min)
sstr = "0" + str(sec)
print(hstr[-2:] + ":" + mstr[-2:] + ":" + sstr[-2:])
