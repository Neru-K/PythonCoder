m = int(input())

if m < 100:
    print('00')
elif m <= 5000:
    print(('0' + str(m))[-4:][0:2])
elif m >= 6000 and m <= 30000:
    print(str(m + 50000)[0:2])
elif m >= 35 and m <= 70:
    print(str((m - 30000) / 5000 + 80000)[0:2])
else:
    print('89')
