A = input()

if len(A) > 1:
    print(A[0 : len(A) - 1])
elif A == "a":
    print(-1)
else:
    print(chr(ord(A) - 1))
