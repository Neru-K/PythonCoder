import re

S = input()

while "ABC" in S:
    S = re.sub("ABC", "", S, 1)

print(S)
