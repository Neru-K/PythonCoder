N = int(input())
S = input()

max_count = 0

cnt_two = 0
cnt_one = 0
cnt_slash = 0

if S[0] == "1":
    cnt_one = 1
elif S[0] == "2":
    cnt_two = 1
elif S[0] == "/":
    cnt_slash = 1

for i in range(1, N):
    char = S[i]
    char_prev = S[i - 1]

    if char_prev == "2" and char != "2" and cnt_slash == 1:
        count = cnt_slash + (min(cnt_one, cnt_two) * 2)
        if count > max_count:
            max_count = count

    elif (char == "1" and char_prev == "/") or (char == "/" and char_prev == "/"):
        cnt_one = 0
        cnt_two = 0
        if cnt_slash > max_count:
            max_count = cnt_slash

    if char == "1":
        cnt_one += 1

        if char_prev == "2":
            cnt_two = 0

        elif char_prev == "/":
            cnt_slash = 0

    elif char == "2":
        cnt_two += 1

        if char_prev == "1":
            cnt_one = 0

    elif char == "/":
        cnt_slash = 1

        if char_prev == "2":
            cnt_two = 0
            cnt_one = 0

print(max_count)
