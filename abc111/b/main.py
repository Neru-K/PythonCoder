N = input()

lst = list(N)
mn = int(min(lst))
mx = int(max(lst))

for i in range(mn, mx + 1):
    if int(N) <= int(str(i) + str(i) + str(i)):
        print(str(i) + str(i) + str(i))
        break
