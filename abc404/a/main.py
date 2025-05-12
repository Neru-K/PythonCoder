alph = set(list('abcdefghijklmnopqrstuvwxyz'))

letters = list(input())

for letter in letters:
  if letter in alph:
    alph.remove(letter)
  
print(list(alph)[0])