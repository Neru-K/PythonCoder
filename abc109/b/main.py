N = int(input())

array = []

for i in range(N):
    s = input()
    array.append(s)

    if i > 0:
        if array[i - 1][-1] != s[0]:
            print("No")
            exit()

if len(array) == len(set(array)):
    print("Yes")
else:
    print("No")