from datetime import datetime

s = input()

point = "2019/4/30"

date1 = datetime.strptime(s, "%Y/%m/%d")
date2 = datetime.strptime(point, "%Y/%m/%d")

if date1 <= date2:
    print("Heisei")
else:
    print("TBD")
