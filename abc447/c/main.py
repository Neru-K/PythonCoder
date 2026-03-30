S = input()
T = input()

S_chars = ["A"]
S_nums = [0]
T_chars = ["A"]
T_nums = [0]

for s in S:
    if len(S_chars) == 1:
        if s != "A":
            S_chars.append(s)
            S_nums.append(1)
        else:
            S_nums[0] += 1

        continue

    if S_chars[-1] != "A" and s != "A":
        S_chars.append("A")
        S_nums.append(0)

    if len(S_chars) > 0 and S_chars[-1] == s:
        S_nums[-1] += 1
    else:
        S_chars.append(s)
        S_nums.append(1)

if S_chars[-1] != "A":
    S_chars.append("A")
    S_nums.append(0)

for t in T:
    if len(T_chars) == 1:
        if t != "A":
            T_chars.append(t)
            T_nums.append(1)
        else:
            T_nums[0] += 1

        continue

    if T_chars[-1] != "A" and t != "A":
        T_chars.append("A")
        T_nums.append(0)

    if T_chars[-1] == t:
        T_nums[-1] += 1
    else:
        T_chars.append(t)
        T_nums.append(1)

if T_chars[-1] != "A":
    T_chars.append("A")
    T_nums.append(0)

if len(S_chars) != len(T_chars):
    print(-1)
    exit()

ans = 0

for i in range(len(S_chars)):
    if S_chars[i] != T_chars[i]:
        print(-1)
        exit()

    ans += abs(S_nums[i] - T_nums[i])

print(ans)
