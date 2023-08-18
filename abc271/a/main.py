N = int(input())

nums = "0123456789ABCDEF"

print(nums[N // 16] + nums[N % 16])
