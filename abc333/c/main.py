N = int(input())

#最初に1,11,111,...111111111111までのリストを作っておく（最大12桁）
digits = [int("1" * (i + 1)) for i in range(12)]
count = 0

for i in range(12):
    for j in range(i + 1):
        for k in range(j + 1):
            count += 1
            if count == N:
                print(digits[i] + digits[j] + digits[k])
                exit()
