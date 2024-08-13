R, G, B = map(int, input().split())
C = input()

dict = {'Red':R, 'Green':G, 'Blue':B}

dict.pop(C)
print(dict.values())

mn = min(dict.values())

print(mn)