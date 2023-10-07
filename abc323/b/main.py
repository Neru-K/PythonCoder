N = int(input())

array = [0] * N

for i in range(N):
    S = input()

    for j in range(N):
        if S[j] == "o":
            array[i] += 1

indexed_numbers = [(num, idx + 1) for idx, num in enumerate(array)]
sorted_indexed_numbers = sorted(indexed_numbers, key=lambda x: x[0], reverse=True)

result = []

for j in range(N):
    result.append(str(sorted_indexed_numbers[j][1]))

print(" ".join(result))
