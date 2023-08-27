N = int(input())

S = [input() for _ in range(N)]

cnt_ac = 0
cnt_wa = 0
cnt_tle = 0
cnt_re = 0

for s in S:
    if s == "AC":
        cnt_ac += 1
    elif s == "WA":
        cnt_wa += 1
    elif s == "TLE":
        cnt_tle += 1
    elif s == "RE":
        cnt_re += 1

print("AC x " + str(cnt_ac))
print("WA x " + str(cnt_wa))
print("TLE x " + str(cnt_tle))
print("RE x " + str(cnt_re))
