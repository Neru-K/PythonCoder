N = int(input())
S = input()

result = "No"


if N % 2 == 0:
    if S[: N // 2] == S[N // 2 :]:
        result = "Yes"

print(result)
