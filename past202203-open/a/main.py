A,B,C = map(int,input().split())

result = [min(A*B,B*C,C*A),max(A*B,B*C,C*A)]
print(*result)