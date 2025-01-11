X = int(input())

sum = 0

for i in range(1, 10):
  for j in range(1, 10):
    times = i * j
    if X == times:
      continue

    sum += times

print(sum)