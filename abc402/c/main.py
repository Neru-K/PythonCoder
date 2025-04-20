# N 食材
# M 料理
# K 料理に使われている食材の種類数
# B 苦手な食材
# https://atcoder.jp/contests/abc402/submissions/65071237


N, M = map(int, input().split())
Ks = []
As = []
idxs = [0] * 9

for i in range(M):
  KA = list(map(int, input().split()))
  K, A = KA[0], KA[1:]
  Ks.append(K)

  As.append(set(A))

B = list(map(int, input().split()))


for b in B:
  eatable = 0
  for seta in As:
    if b in seta:
      seta.remove(b)

    if len(seta) == 0:
      eatable += 1

  print(eatable)