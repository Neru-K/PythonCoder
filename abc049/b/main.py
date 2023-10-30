H, W = map(int, input().split())

result = ""

for i in range(H):
    s = input()
    result += s + "\n" + s + "\n"

print(result.strip())
