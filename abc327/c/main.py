rows = [{i: False for i in range(1, 10)} for _ in range(9)]
cols = [{i: False for i in range(1, 10)} for _ in range(9)]
squares = [{i: False for i in range(1, 10)} for _ in range(9)]

for i in range(9):
    A = list(map(int, input().split()))
    for j in range(9):
        num = A[j]
        rows[i][num] = True
        cols[j][num] = True

        # どの3x3のマス目かを特定
        square_index = (i // 3) * 3 + j // 3
        squares[square_index][num] = True

result = "Yes"

for arr in [rows, cols, squares]:
    for d in arr:
        if all(d.values()) == False:
            result = "No"
            break

print(result)
