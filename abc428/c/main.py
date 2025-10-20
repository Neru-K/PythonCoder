Q = int(input())

LR = {"(": 0, ")": 0}
prev = ""
stack = []
stack2 = []

for _ in range(Q):
    i, *listc = map(str, input().split())

    if i == "1":
        c = listc[0]
        LR[c] += 1
        prev = c
        stack.append(c)

        if len(stack2) == 0:
            stack2.append(0)
        elif stack2[-1] == 0:
            stack2.append(0)

        elif LR["("] == LR[")"]:
            if len(stack) == 0:
                stack.append(1)
            elif stack[0] == "(" and stack[len(stack) - 1] == ")":
                stack.append(1)
            else:
                stack.append(0)
        else:
            stack.append(0)

        if len(stack2) == 0 or stack2[-1] == 1:
            print("Yes")
        else:
            print("No")

    else:
        LR[prev] -= 1
        del stack[-1]
        del stack2[-1]
        if len(stack) == 0:
            print("Yes")
        elif stack[-1] == 1:
            print("Yes")
        else:
            print("No")
