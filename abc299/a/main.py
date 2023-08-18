N = int(input())
S = input()

left = -1
right = -1
treasure = -1

for i in range(N):
    if left < 0 and S[i] == "|":
        left = i
    elif left > -1 and S[i] == "|":
        right = i
    elif S[i] == "*":
        treasure = i

if treasure > left and treasure < right:
    print("in")
else:
    print("out")
