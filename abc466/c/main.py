N = int(input())


def qa(i, j):
    print(f"? {i + 1} {j + 1}", flush=True)
    a = input()
    return a


def shakutori(N):
    j = 1
    ans = 0
    for i in range(N - 1):
        if j <= i:
            j = i + 1

        while j < N and qa(i, j) == "Yes":
            j += 1

        ans += j - i - 1

    return ans


print(f"! {shakutori(N)}", flush=True)
