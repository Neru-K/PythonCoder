nums = list(map(int, input().split()))
k = int(input())

nums.sort()

print(nums[0] + nums[1] + nums[2] * (2 ** k))
