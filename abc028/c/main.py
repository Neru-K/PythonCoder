NUMS = list(map(int, input().split()))

nums = []

for i in range(0, 5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            nums.append(NUMS[i] + NUMS[j] + NUMS[k])

unique = list(set(nums))
unique.sort()

print(unique[len(unique) - 3])
