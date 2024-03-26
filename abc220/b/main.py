K = int(input())
A,B = map(str,input().split())

def convertToTen(str, n):
    l = list(str)
    sum = 0
    count = 0
    for i in range(len(l)-1, -1, -1):
        sum += (n ** count) * int(l[i])
        count += 1
        
    return sum

num1 = convertToTen(A,K)
num2 = convertToTen(B,K)

print(num1 * num2)