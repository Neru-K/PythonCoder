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
    Char = S[i]
    Char_prev = S[i - 1]
    if Char == "1":
        cnt_one += 1

    elif Char == "2":
        cnt_two += 1

        if Char_prev == "1":
            cnt_one = 0

    elif Char == "/":
        cnt_slash = 1
        
        if Char_prev == "2":
            count = max(cnt_slash, cnt_one, cnt_two)
            if count > max_count:
                max_count = count
            count = 0

print(max_count)
