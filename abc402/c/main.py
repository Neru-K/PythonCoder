# N 食材
# M 料理
# K 料理に使われている食材の種類数
# B 苦手な食材
# https://atcoder.jp/contests/abc402/submissions/65071237


N, M = map(int, input().split())
Ks = []
As = []
list_count = [0] * N

# まずは食材と、その食材が最初に食べられる日の対応を作る。

# ループで各料理の食材を見ていって、その料理の食材において、最後に食べられる日を確認→配列に＋1する

for i in range(M):
  KA = list(map(int, input().split()))
  K, A = KA[0], KA[1:]
  Ks.append(K)

  As.append(set(A))

B = list(map(int, input().split()))

dict = {}

for i in range(N):
  dict[B[i]] = i
  

for list_a in As:
  max = -1
  for a in list_a:
    if dict[a] > max:
      max = dict[a]
      
  list_count[max] += 1
  
count = 0

for c in list_count:
  count += c
  print(count)