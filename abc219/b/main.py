S1 = input()
S2 = input()
S3 = input()

array_s = [S1, S2, S3]

nums = list(input())

result = ""

for i in nums:
    result += array_s[int(i) - 1]

print(result)