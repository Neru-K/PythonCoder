s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s3, e3 = map(int, input().split())

sum1 = s1 * (e1 / 10)
sum2 = s2 * (e2 / 10)
sum3 = s3 * (e3 / 10)

print(int(sum1 + sum2 + sum3))
