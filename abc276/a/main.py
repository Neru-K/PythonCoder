s = input()

last_index = s.rfind("a")
if last_index >= 0:
    last_index += 1

print(last_index)
