N = int(input())
first = ["H" , "D" , "C" , "S"]
second = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]

set_s = set()

for i in range(N):
    S = input()
    if S[0] in first and S[1] in second and S not in set_s:
        set_s.add(S)
    else:
        print("No")
        exit()

print("Yes")