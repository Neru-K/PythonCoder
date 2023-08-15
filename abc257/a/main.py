N, X = map(int, input().split())

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_chars = ""

for i in range(N):
    new_chars += chars

sorted_str = "".join(sorted(new_chars))

print(sorted_str[X - 1])
