s = input()

new_s = []

for i in range(0,len(s),2):
    new_s.append(s[i])

print("".join(new_s))