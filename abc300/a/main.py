N ,A ,B = map(int, input().split())
C = list(map(int, input().split()))

for i ,num in enumerate(C):
    if num == A + B:
        print(i + 1)
