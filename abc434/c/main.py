# それぞれで上限と下限を考える。
# ひとつでも範囲が重ならないところがあれば、Noとなる。
T = int(input())


def solve():
    N, H = map(int, input().split())
    tlu = []
    for _ in range(N):
        t, l, u = map(int, input().split())
        tlu.append((t, l, u))

    prev_t = 0
    range_high = H
    range_low = H

    for t, l, u in tlu:
        range_high += t - prev_t
        range_low -= t - prev_t
        range_low = max(range_low, 1)

        if min(l, u) > max(range_high, range_low) or min(range_high, range_low) > max(
            l, u
        ):
            print("No")
            return

        range_high = min(range_high, u)
        range_low = max(range_low, l)

        """ if range_high < range_low:
            print("No")
            return """
        prev_t = t

    print("Yes")


for _ in range(T):
    solve()
