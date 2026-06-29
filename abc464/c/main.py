# 方針 1匹しかいない鳥が減ったら ans -= 1 0匹しかいない鳥が増えたら ans+= 1

N, M = map(int, input().split())

birds = [0] * N  # 色別で鳥が何匹ずついるかを記録
ans = 0
results = [0] * M

cases = []

for i in range(N):
    A, D, B = map(int, input().split())
    A -= 1
    D -= 1
    B -= 1

    cases.append([A, D, B])
    birds[A] += 1
    if birds[A] == 1:
        ans += 1

results[0] = ans

cases.sort(key=lambda x: x[1])


for A, D, B in cases:
    birds[A] -= 1
    if birds[A] == 0:
        ans -= 1

    birds[B] += 1
    if birds[B] == 1:
        ans += 1

    results[D] = ans

prev = 0

for r in results:
    if r == 0:
        print(prev)

    else:
        print(r)
        prev = r
