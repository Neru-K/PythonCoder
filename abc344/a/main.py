import re
S = input()

print(re.sub('\|.*?\|','',S))