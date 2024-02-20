""" 
考えたこと


"""

def main():
    m = int(input())
    s = [input() for _ in range(3)]
    flag = [[False] * 10 for _ in range(3)]
    no = []

    for i in range(10):
        for j in range(3):
            for k in range(m):
                if s[j][k] == str(i):
                    flag[j][k] = True

    for i in range(10):
        if not (flag[0][i] and flag[1][i] and flag[2][i]):
            no.append(i)

    num = [0, 1, 2]
    mn = float('inf')

    for i in range(10):
        noflag = i in no
        if noflag:
            continue

        ans = -1
        for perm in permutations(num):
            for j in range(3):
                for k in range(ans + 1, m * 3):
                    if s[perm[j]][k % m] == str(i):
                        ans += k
                        break
        mn = min(mn, ans)

    print(mn)

if __name__ == "__main__":
    main()