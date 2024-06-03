N = input()

idx = -1

count = 0

nextflag = False

for i in range(1,len(N)):
    if nextflag:
        nextflag = False
        continue

    current = int(N[i])
    prev = int(N[i - 1])
    if abs(current - prev) > 1:
        count += 1
        if count > 1:
            print("No")
            exit()

        L = prev + 1
        M = prev
        S = prev - 1

        if i < int(len(N)) - 1:
            next = int(N[i + 1])
            if abs(prev - L) <= 1 and abs(next - L) <= 1:
                nextflag = True
                continue
            elif abs(prev - M) <= 1 and abs(next - M) <= 1:
                nextflag = True
                continue
            elif abs(prev - S) <= 1 and abs(next - S) <= 1:
                nextflag = True
                continue
            else:
                print("No")
                exit()
        else:
            if abs(prev - L) <= 1:
                continue
            elif abs(prev - M) <= 1:
                continue
            elif abs(prev - S) <= 1:
                continue
            else:
                print("No")
                exit()

print("Yes")
