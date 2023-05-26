V, *ABC = map(int, input().split())
sum = 0

while True:
    sum += ABC[0]
    if sum > V:
        print("F")
        break
    sum += ABC[1]
    if sum > V:
        print("M")
        break
    sum += ABC[2]
    if sum > V:
        print("T")
        break
