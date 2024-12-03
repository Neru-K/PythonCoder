N = int(input())
S = input()

max_count = 0

cnt_two = 0
cnt_one = 0
cnt_slash = 0

for i in range(N):
    Char = S[i]
    if Char == "1":
        cnt_one += 1
        if i != N - 1:
            if Char == "1" or Char == "/":
                cnt_one = 0

    elif Char == "2":
        cnt_two += 1

    elif Char == "/":
        if cnt_slash == 0:
            cnt_slash += 1
        else:
            max_count = max(max_count, 1)
            cnt_one = 0
            cnt_two = 0
