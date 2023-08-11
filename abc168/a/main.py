N = input()

pon = ["0", "1", "6", "8"]
bon = ["3"]


if N[len(N) - 1] in pon:
    print("pon")
elif N[len(N) - 1] in bon:
    print("bon")
else:
    print("hon")
