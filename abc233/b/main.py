L, R = map(int, input().split())
S = input()

left = S[0 : L - 1]
mid = S[L - 1 : R]
right = S[R:]

print(left + mid[::-1] + right)
