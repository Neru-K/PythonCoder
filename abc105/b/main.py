N = int(input())

for i in range(101):
    for j in range(101):
        if i * 4 + j * 7 == N:
            print("Yes")
            exit()

print("No")