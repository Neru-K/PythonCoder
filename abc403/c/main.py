# N ユーザー人数
# M コンテストページの数
# 1 X Y ユーザーXにコンテストページYの閲覧権限付与
# 2 X ユーザXに全てのコンテストページの閲覧権限付与
# 3 X Y ユーザーXがコンテストページYを閲覧できるか答える

N, M, Q = map(int, input().split())

dict = {}
all = set()

for i in range(Q):
  query = input()
  
  q, x, y = None, None, None
  if query[0] == "2":
    q, x = map(int, query.split())
  else:
    q, x, y = map(int, query.split())
  
  if q == 1:
    if x in dict:
      dict[x].add(y)
    else:
      dict[x] = set([y])

  elif q == 2:
    all.add(x)
  else:
    if x in all:
      print("Yes")
    elif x in dict and y in dict[x]:
      print("Yes")
    else:
      print("No")