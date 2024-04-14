S = input()

setS = list(set(list(S)))

counts = [0] * 100

for i in range(len(setS)):
    cnt = S.count(setS[i])
    counts[cnt - 1] += 1

for i in range(len(counts)):
    if counts[i] != 0 and counts[i] != 2:
        print("No")
        exit()
        
print("Yes")