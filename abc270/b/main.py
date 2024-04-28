X, Y, Z = map(int,input().split())
O = 0

mn = min(X, Y, Z)

if mn < 0:
    X += (0 - mn)
    Y += (0 - mn)
    Z += (0 - mn)
    O += (0 - mn)

mn2 = min(X, Y, Z, O)

if mn2 == O:
    if X < Y and X < Z:
        print(X - O)
    elif Y < X and Y < Z:
        print(-1)
    elif Z < X and Z < Y:
        print(X - O)

elif mn2 == X:
    if Y < Z and Z < O:
        print(O - X)
    elif Y < O and O < Z:
        print((Z - O) + (Z - X))
    elif Z < Y and Y < O:
        print(-1)
    elif Z < O and O < Y:
        print(O - X)
    elif O < Y and O < Z:
        print(O - X)

elif mn2 == Y:
    if O < X and O < Z:
        print(X - O)
    elif X < O and X < Z:
        print(O - X)
    elif Z < O and Z < X:
        print(abs(X - O))

else:
    if O < X and X < Y:
        print(X - O)
    elif O < Y and Y < X:
        print((O - Z) + (X - Z))
    elif X < O and O < Y:
        print(O - X)
    elif X < Y and Y < O:
        print(-1)
    elif Y < O and Y < X:
        print(abs(X - O))