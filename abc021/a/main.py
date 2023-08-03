n = int(input())

nums = [8, 4, 2, 1]

result = ""

count = 0
i = 0

while n > 0:
    if n % nums[i] == n:
        i += 1
    else:
        for _ in range(n // nums[i]):
            if count > 0:
                result += "\n"
            result += str(nums[i])
            count += 1
        n -= nums[i]

print(count)
print(result)
