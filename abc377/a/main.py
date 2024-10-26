S = list(input())
S.sort()
S = ''.join(S)

ABC = list("ABC")
ABC.sort()
ABC = ''.join(ABC)



if ABC == S:
    print("Yes")
else:
    print("No")