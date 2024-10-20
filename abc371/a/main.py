S1,S2,S3 = map(str, input().split())

if S1 == "<":
    if S2 == "<":
        if S3 == "<":
            print('B')
        else:
            print('C')
    else:
        if S3 == ">":
            print("A")

else:
    if S2 == "<":
        if S3 == "<":
            print("A")

    else:
        if S3 == ">":
            print("B")
        else:
            print("C")