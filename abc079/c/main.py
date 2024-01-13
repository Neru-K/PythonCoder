S = list(input())
A, B, C, D = int(S[0]), int(S[1]), int(S[2]), int(S[3])

if A + B + C + D == 7:
    print(f"{S[0]}+{S[1]}+{S[2]}+{S[3]}=7")
elif A + B + C - D == 7:
    print(f"{S[0]}+{S[1]}+{S[2]}-{S[3]}=7")
elif A + B - C + D == 7:
    print(f"{S[0]}+{S[1]}-{S[2]}+{S[3]}=7")
elif A + B - C - D == 7:
    print(f"{S[0]}+{S[1]}-{S[2]}-{S[3]}=7")
elif A - B + C + D == 7:
    print(f"{S[0]}-{S[1]}+{S[2]}+{S[3]}=7")
elif A - B - C + D == 7:
    print(f"{S[0]}-{S[1]}-{S[2]}+{S[3]}=7")
elif A - B + C - D == 7:
    print(f"{S[0]}-{S[1]}+{S[2]}-{S[3]}=7")
elif A - B - C - D == 7:
    print(f"{S[0]}-{S[1]}-{S[2]}-{S[3]}=7")
