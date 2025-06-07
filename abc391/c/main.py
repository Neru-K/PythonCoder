N, Q = map(int, input().split())

nest = [1] * N  # 巣に何匹いるか
position_p = []

for p in range(N):
    position_p.append(p)

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        P, H = q[1], q[2]
        # 今いる巣を取り出す。
        position_p[P - 1] = H - 1
        nest[P - 1] -= 1
        nest[H - 1] += 1

        # ansを持っておいて、クエリ1の時には更新しておく。クエリ2でそれを出力するだけ。

        # 巣にいる鳩が1匹から2匹になったタイミング、もしくは2匹が1匹になったタイミングが鍵。

    else:
        print()
