X = int(input())

fivehundreds = X // 500
five = (X % 500) // 5

print(fivehundreds * 1000 + five * 5)
