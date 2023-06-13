x, y = input().split()

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

if dic[x] == dic[y]:
    print("=")
elif dic[x] > dic[y]:
    print(">")
else:
    print("<")
