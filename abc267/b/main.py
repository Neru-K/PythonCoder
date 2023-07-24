s = input()
result = "No"
cols = [int(s[6]), int(s[3]), int(s[1]+s[7]), int(s[0]+s[4]),
        int(s[2]+s[8]), int(s[5]), int(s[9])]

if int(s[0]) == 0:
    if cols[2] == 0 and (cols[0] + cols[1]) > 0 and (cols[3] + cols[4] + cols[5] + cols[6]) > 0:
        result = "Yes"
    elif cols[3] == 0 and (cols[0] + cols[1] + cols[2]) > 0 and (cols[4] + cols[5] + cols[6]) > 0:
        result = "Yes"
    elif cols[4] == 0 and (cols[0] + cols[1] + cols[2] + cols[3]) > 0 and (cols[5] + cols[6]) > 0:
        result = "Yes"

print(result)
