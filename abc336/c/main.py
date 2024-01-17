N = int(input()) - 1

nums = ["0", "2", "4", "6", "8"]

result = []

isFirst = True

while N >= 0:
    result.append(nums[N % 5])

    N = N // 5

result.reverse()

print(int("".join(result)))
