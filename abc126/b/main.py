S = input()
L = int(S[0:2])
R = int(S[2:4])

if L >= 1 and L <= 12:
    if R >= 1 and R <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")

else:
    if R >= 1 and R <= 12:
        print("YYMM")
    else:
        print("NA")
