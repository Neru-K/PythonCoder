import re

N = int(input())
S = input()
pattern = '\/\*.*?\*\/'
repatter = re.compile(pattern)

print(re.sub(repatter,'',S))