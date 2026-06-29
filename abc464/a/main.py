S = input()

count = [0,0] # E, W

for c in S:
  if c == 'E':
    count[0] += 1
  else:
    count[1] += 1

if count[0]  > count[1]:
  print('East')
else:
  print('West')