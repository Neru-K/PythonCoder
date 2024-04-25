S1 = input()
S2 = input()
S3 = input()

sets = set([S1,S2,S3])

if "ABC" not in sets:
    print("ABC")
elif "ARC" not in sets:
    print("ARC")
elif "AGC" not in sets:
    print("AGC")
else:
    print("AHC")