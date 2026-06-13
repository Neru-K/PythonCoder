N, K, M = map(int, input().split())

list_vc = []


for i in range(N):
  C, V = map(int, input().split())
  list_vc.append([V,C])

list_vc.sort(key=lambda x: -x[0])

print(list_vc)

setc = {} # 現在のCの種類数（list_vcからVが大きいものを選択していったとき）

for j in range(K):
  setc.add(list_vc[j][1])

while len(setc) < M:


# 大きい方からK個の中から、何を出して、何を入れるかの条件を考える
# 単純に一番小さいものを出し、一番大きいものを入れる、だけでは足りなさそう
# 加えて、大きい方からKこの中で色の重複があるものを出し、色がないものを入れる、でOKか？