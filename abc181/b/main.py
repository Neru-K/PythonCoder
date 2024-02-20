N = int(input())
sum = 0

for i in range(N):
    A,B = map(int,input().split())
    num = B - A + 1
    if num % 2 ==0:
        sum += (B + A) * num // 2
    else:
        sum += (B + A) * ((num - 1) // 2) + ((B + A) // 2)

print(sum)
