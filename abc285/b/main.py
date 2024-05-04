N = int(input())
S = input()

for gap in range(1, N):
    base = 0
    count = 0

    while base + gap < N:
        if S[base] == S[base + gap]:
            break
        else:
            count += 1

        base += 1

    print(count)