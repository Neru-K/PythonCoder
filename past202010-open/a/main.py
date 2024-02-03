A, B, C = map(int, input().split())

array = [(A, "A"), (B, "B"), (C, "C")]

sorted_lst = sorted(array, key=lambda x: x[0])

print(sorted_lst[1][1])