from decimal import Decimal, getcontext

D = int(input())
getcontext().prec = D

A = Decimal(input())
B = Decimal(input())

result = A + B

output = result.quantize(Decimal("1." + "0" * D))
print(output)
