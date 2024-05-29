N = int(input())

isPerfect = False
isGreat = False

sets = set()

for i in range(N):
    s = input()
    sets.add(s)

lst = list(sets)

lst.sort()

if len(lst) == 1:
    if lst[0] == "Perfect":
        print("All Perfect ")
        exit()
    if lst[0] == "Great":
        print("Full Combo")
        exit()
    
elif len(lst) == 2:
    if lst[0] == "Great" and lst[1] == "Perfect":
        print("Full Combo")
        exit()
    

print("Failed")