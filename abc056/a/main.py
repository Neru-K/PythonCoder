a, b = map(str, input().split())

if a == "H":
    if b == "H":  # TopCoDeerくんは正直者だ
        print("H")
    elif b == "D":  # TopCoDeerくんは嘘つきだ
        print("D")

elif a == "D":
    if b == "H":  # TopCoDeerくんは正直者だ
        print("D")
    elif b == "D":  # TopCoDeerくんは嘘つきだ
        print("H")
