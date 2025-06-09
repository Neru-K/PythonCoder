N, Q = map(int, input().split())

nest = [1] * N  # 巣に何匹いるか（数）
position_p = []  # それぞれの鳩がどこにいるか（インデックス）

for p in range(N):
    position_p.append(p)

ans = 0

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        P, H = q[1], q[2]  # クエリ。鳩Pを巣Hに移動させるという指示。
        position_before = position_p[P - 1]  # 鳩Pが今いる巣を取り出す。
        position_p[P - 1] = H - 1  # 鳩Pを巣Hに移動させる。

        nest[position_before] -= 1  # 移動元の巣の数を減らす
        if nest[position_before] == 1:
            ans -= 1
        nest[H - 1] += 1  # 移動先の巣の数を増やす
        if nest[H - 1] == 2:
            ans += 1

        # ansを持っておいて、クエリ1の時には更新しておく。クエリ2でそれを出力するだけ。
        # 巣にいる鳩が1匹から2匹になったタイミング、もしくは2匹が1匹になったタイミングが鍵。

    else:
        print(ans)
