T = input()
U = input()

start = 0

flag = False
while start + len(U) <= len(T):
  for i in range(len(U)):
    if T[i + start] == "?":
      flag = True
      continue
    elif T[i + start] == U[i]:
      flag = True
      continue
    else:
      flag = False
      break

  start+= 1
  if flag:
    break
  
if flag:
  print("Yes")
else:
  print("No")